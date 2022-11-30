from publicsuffix2 import *

class UrlHandle(object):

    def HttpOrHttpsHandle(self,url):
        url = url.replace('http://','')
        url = url.replace('https://', '')
        return url

    def DomainHandle(self,url):
        url = get_sld(url)
        return url

    def HandleUrl(self,url):
        url = self.DomainHandle(self.HttpOrHttpsHandle(url))
        return url

if __name__ == '__main__':
    test = UrlHandle()
    print(test.HandleUrl('https://www.6151027.com'))

