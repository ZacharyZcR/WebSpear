from concurrent.futures import ThreadPoolExecutor
from tools.module import *
from tqdm import tqdm

class DirFuzz(Config, FileIO, UrlHandle):

    def __init__(self):
        super().__init__()
        self.dictionary = self.FileReadInList('../config/top7000.txt')
        self.max_workers = 10

        self.target = self.HandleUrl(self.target)
        self.http_flag = None
        self.https_flag = None
        self.protocol = None

        self.target_length_list = []
        self.target_status_list = []
        self.target_list = []
        self.target_length_dec_list = []
        self.result = []

    def GetTargetStatusAndLength(self,param):
        try:
            s = requests.session()
            s.keep_alive = False
            req = s.get(url = self.protocol + self.target + param,
                               headers = self.headers,
                               proxies = self.proxies,
                               timeout = self.timeout)
            target_length = len(req.text)
            target_status = req.status_code
            return target_length,target_status,param
        except Exception as e:
            pass

    def DirScan(self):
        if self.http_flag == False and self.https_flag == False:
            return 0

        if self.http_flag:
            self.protocol = 'http://'
            with ThreadPoolExecutor(max_workers = self.max_workers) as executor:
                result = list(tqdm(executor.map(self.GetTargetStatusAndLength,self.dictionary),total = len(self.dictionary)))
        if self.https_flag:
            self.protocol = 'https://'
            with ThreadPoolExecutor(max_workers = self.max_workers) as executor:
                result = list(tqdm(executor.map(self.GetTargetStatusAndLength,self.dictionary),total = len(self.dictionary)))

        for element in result:
            try:
                self.target_length_list.append(element[0])
                self.target_status_list.append(element[1])
                self.target_list.append(element[2])
            except:
                pass

    def DirHandle(self):
        try:
            dec_list = []
            average = int(sum(self.target_length_list) / len(self.target_length_list))
            for element in self.target_length_list:
                dec_list.append(abs(element - average))
            dec_zipped = zip(self.target_list,self.target_status_list,dec_list)
            sorted_zip = sorted(dec_zipped, key = lambda x:x[2],reverse = True)
            sorted_target_list,sorted_target_stauts_list,sorted_dec_list = zip(*sorted_zip)

            self.target_list = sorted_target_list
            self.target_length_dec_list = sorted_dec_list
            self.target_status_list = sorted_target_stauts_list

            return self.target_list,self.target_length_dec_list,self.target_status_list

        except Exception as e:
            print(e)

    def DirResult(self):
        for i in range(len(self.target_list)):
            self.result.append(f"{self.target_list[i]} - {self.target_status_list[i]} - {self.target_length_dec_list[i]}")

    def DirReport(self):
        try:
            for element in self.result:
                print(element)
        except Exception as e:
            print(e)
            pass

    def DirStore(self,filename):
        try:
            self.FileWriteInTxt(self.result, filename)
        except Exception as e:
            pass

    def test(self):
        with ThreadPoolExecutor(max_workers = self.max_workers) as executor:
            result = list(tqdm(executor.map(self.GetTargetStatusAndLength,self.dictionary),total = len(self.dictionary)))
        for element in result:
            print(element)

if __name__ == '__main__':
    test = DirFuzz()
    test.HttpOrHttps()
    test.DirScan()
    test.DirHandle()
    test.DirResult()
    test.DirStore('test1.txt')
    test.DirReport()
