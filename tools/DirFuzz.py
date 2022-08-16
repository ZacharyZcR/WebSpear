import requests

class DirFuzz(object):

    def __int__(self):
        self.headers = {}
        self.proxies = {
            'http:':None,
            'https:':None,
        }
        self.timeout = 0
        self.target = ''

    def __SelectHeaders(self,headers):
        self.headers = headers

    def __SelectProxies(self,proxies):
        self.proxies = proxies

    def __SelectTimeout(self,timeout):
        self.timeout = timeout

    def __SelectTarget(self,target):
        self.target = target

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

    def 

