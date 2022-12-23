from publicsuffix2 import *
import re

class UrlHandle(object):

    def HttpOrHttpsHandle(self, url):
        # 使用正则表达式替换URL中的协议类型
        url = re.sub(r'^https?://', '', url)
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

