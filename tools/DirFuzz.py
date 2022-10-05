from concurrent.futures import ThreadPoolExecutor
import requests

class DirFuzz(object):

    def __init__(self):
        self.headers = {}
        self.proxies = {
            'http:':None,
            'https:':None,
        }
        self.timeout = 1
        self.target = 'http://www.baidu.com/'
        self.dictionary = ['aaa','aaa','aaa','aaa','aaa']
        self.max_workers = 5

        self.target_length_list = []
        self.target_status_list = []

    def __SelectHeaders(self,headers):
        self.headers = headers

    def __SelectProxies(self,proxies):
        self.proxies = proxies

    def __SelectTimeout(self,timeout):
        self.timeout = timeout

    def __SelectTarget(self,target):
        self.target = target

    def __SelectDictionary(self,dictionary):
        self.dictionary = dictionary

    def __SelectMaxWorkers(self,max_workers):
        self.max_workers = max_workers

    def GetTargetStatusAndLength(self,param):
        try:
            req = requests.get(url =self.target + param,
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
            result = list(executor.map(self.GetTargetStatusAndLength,self.dictionary))
        for element in result:
            print(element)

if __name__ == '__main__':
    test = DirFuzz()
    test.test()
