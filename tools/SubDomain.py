from concurrent.futures import ThreadPoolExecutor
import requests
from publicsuffix2 import get_public_suffix

class SubDomain():

    def __init__(self):
        super().__init__()
        self.dictionary = ['aaa', 'aaa', 'aaa', 'aaa', 'aaa']
        self.max_workers = 5

        self.target_length_list = []
        self.target_status_list = []

    def __SelectHeaders(self, headers):
        self.headers = headers

    def __SelectProxies(self, proxies):
        self.proxies = proxies

    def __SelectTimeout(self, timeout):
        self.timeout = timeout

    def __SelectTarget(self, target):
        target = get_public_suffix(target)
        print(target)
        self.target = target

    def __SelectDictionary(self, dictionary):
        self.dictionary = dictionary

    def __SelectMaxWorkers(self, max_workers):
        self.max_workers = max_workers

    def FuzzSubDomain(self, param):
        try:
            req = requests.get(url=,
                               headers=self.headers,
                               proxies=self.proxies,
                               timeout=self.timeout)
            target_length = len(req.text)
            target_status = req.status_code
            return target_length, target_status
        except Exception as e:
            print(e)
            return 'Error','Error'

    def 