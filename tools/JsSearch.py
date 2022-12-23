import requests
# import bs4

class JsSearch(object):

    def __init__(self):
        self.headers = {}
        self.proxies = {
            'http:': None,
            'https:': None,
        }
        self.timeout = 1
        self.target = 'http://www.baidu.com/'
        self.content = ''

    def GetHtml(self):
        try:
            req = requests.get(url=self.target,
                               headers=self.headers,
                               proxies=self.proxies,
                               timeout=self.timeout)
            content = req.text
            self.content = content
        except Exception as e:
            print(e)
            return 'Error', 'Error'
    #
    # def SearchInHtml(self):
    #
    # def SearchInJs(self):

