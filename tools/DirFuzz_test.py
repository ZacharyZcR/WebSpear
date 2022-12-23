import requests
from concurrent.futures import ThreadPoolExecutor
import json

class DirFuzz:
    def __init__(self, base_url, wordlist_file, headers=None, timeout=5, proxies=None, max_workers=20):
        self.base_url = base_url
        self.wordlist_file = wordlist_file
        self.headers = headers or {}
        self.timeout = timeout
        self.proxies = proxies or {}
        print(self.proxies)
        self.max_workers = max_workers
        self.wordlist = []

    def load_wordlist(self):
        with open(self.wordlist_file, "r") as f:
            for line in f:
                self.wordlist.append(line.strip())

    def scan(self):
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for word in self.wordlist:
                url = f"{self.base_url}{word}"
                future = executor.submit(self.check_url, url)
                (lambda current_url: future.add_done_callback(
                    lambda future: self.handle_response(future, current_url, results)))(url)
        return json.dumps(results)

    def check_url(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout, proxies=self.proxies)
            return response.status_code
        except Exception:
            return None

    def handle_response(self, future, url, results):
        status_code = future.result()
        response = {
            'url': url,
            'status_code': status_code
        }
        results.append(response)

if __name__ == "__main__":
    fuzzer = DirFuzz(base_url="https://6151027.com", wordlist_file="../config/top7000.txt",
                     headers={
                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"},
                     timeout=1,)
    fuzzer.load_wordlist()
    print(fuzzer.scan())