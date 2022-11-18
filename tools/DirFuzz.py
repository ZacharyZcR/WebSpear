from concurrent.futures import ThreadPoolExecutor
from  module import *
import tqdm
import os

class DirFuzz(HttpConfig,FileIO):

    def __init__(self):
        super().__init__()
        self.dictionary = self.FileReadInList('../test.txt')
        print(self.dictionary)
        self.max_workers = 5

        self.target_length_list = []
        self.target_status_list = []

    def __SelectDictionary(self,dictionary):
        self.dictionary = dictionary

    def __SelectMaxWorkers(self,max_workers):
        self.max_workers = max_workers

    def GetTargetStatusAndLength(self,param):
        try:
            s = requests.session()
            s.keep_alive = False
            req = s.get(url =self.target + param,
                               headers = self.headers,
                               proxies = self.proxies,
                               timeout = self.timeout)
            target_length = len(req.text)
            target_status = req.status_code
            return target_length,target_status
        except Exception as e:
            print(e)
            return 'Error','Error'

    def Scan(self):
        with ThreadPoolExecutor(max_workers = self.max_workers) as executor:
            result = list(executor.map(self.GetTargetStatusAndLength,self.dictionary))
        for element in result:
            self.target_length_list.append(element[0])
            self.target_status_list.append(element[1])

    def test(self):
        with ThreadPoolExecutor(max_workers = self.max_workers) as executor:
            result = list(tqdm(executor.map(self.GetTargetStatusAndLength,self.dictionary),total = len(self.dictionary)))
        for element in result:
            print(element)

if __name__ == '__main__':
    test = DirFuzz()
    print(test.target)
    test.test()
