import requests
import configparser
import json

class HttpConfig(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config/example.ini')
        self.headers = json.loads(config["HttpConfig"]["headers"])
        self.proxies = json.loads(config["HttpConfig"]["proxies"])
        self.timeout = int(config["HttpConfig"]["timeout"])
        self.target = config["HttpConfig"]["target"]

    def test(self):
        print('test')

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config["HttpConfig"] = {}
    config["HttpConfig"]["headers"] = '{}'
    config["HttpConfig"]["proxies"] = '{"http:": "None","https:": "None"}'
    config["HttpConfig"]["timeout"] = '1'
    config["HttpConfig"]["target"] = 'http://www.baidu.com/'
    config.write(open('../config/example.ini', 'w'))
    # config.read('../config/example.ini')
    # config["DirFuzz"]
    # headers = json.loads(config["HttpConfig"]["headers"])
    # proxies = json.loads(config["HttpConfig"]["proxies"])
    # timeout = int(config["HttpConfig"]["timeout"])
    # target = config["HttpConfig"]["target"]
    # print(type(proxies))
    # print(proxies)
    # r = requests.get(url = target,headers = headers,proxies = proxies,timeout = timeout)
    # print(r.text)

