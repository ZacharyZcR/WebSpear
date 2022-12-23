from concurrent.futures import ThreadPoolExecutor
from tools.module import *
from tqdm import tqdm

class SubDomain(Config, FileIO):

    def __init__(self):
        super().__init__()
        self.dictionary = self.FileReadInList('../config/domain.txt')
        self.max_workers = 10

        self.target_length_list = []
        self.target_status_list = []
        self.target_list = []
        self.target_length_dec_list = []
        self.result = []

    def __SelectDictionary(self, dictionary):
        self.dictionary = dictionary

    def __SelectMaxWorkers(self, max_workers):
        self.max_workers = max_workers

    def GetDomain(self):
        self.target = get_sld(self.target)
        print(self.target)

    def FuzzSubDomain(self, param):
        try:
            s = requests.session()
            s.keep_alive = False
            req = s.get(url='https://' + param + self.target,
                               headers=self.headers,
                               proxies=self.proxies,
                               timeout=self.timeout)
            target_length = len(req.text)
            target_status = req.status_code
            print(req.status_code)
            return target_length, target_status, param
        except Exception as e:
            print('https://' + param + self.target)
            pass

    def SubDomainScan(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            result = list(tqdm(executor.map(self.FuzzSubDomain, self.dictionary), total=len(self.dictionary)))
        for element in result:
            try:
                self.target_length_list.append(element[0])
                self.target_status_list.append(element[1])
                self.target_list.append(element[2])
            except:
                pass

    def SubDomainHandle(self):
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

    def SubDomainResult(self):
        for i in range(len(self.target_list)):
            self.result.append(f"{self.target_list[i]} - {self.target_status_list[i]} - {self.target_length_dec_list[i]}")

    def SubDomainReport(self):
        try:
            for element in self.result:
                print(element)
        except Exception as e:
            print(e)
            pass

if __name__ == '__main__':
    test = SubDomain()
    test.GetDomain()
    test.SubDomainScan()
    test.SubDomainHandle()
    test.SubDomainResult()
    test.SubDomainReport()