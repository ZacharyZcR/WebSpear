from concurrent.futures import ThreadPoolExecutor
from module import *
from tqdm import tqdm
from publicsuffix2 import get_public_suffix

class SubDomain(HttpConfig,FileIO):

    def __init__(self):
        super().__init__()
        self.dictionary = self.FileReadInList('../config/top7000.txt')
        self.max_workers = 10

        self.target_length_list = []
        self.target_status_list = []
        self.target_list = []
        self.target_length_dec_list = []

    def __SelectDictionary(self, dictionary):
        self.dictionary = dictionary

    def __SelectMaxWorkers(self, max_workers):
        self.max_workers = max_workers

    def FuzzSubDomain(self, param):
        try:
            s = requests.session()
            s.keep_alive = False
            req = s.get(url=,
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