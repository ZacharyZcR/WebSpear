from tools import *

class Main():

    def __init__(self):
        self.config = Config()
        self.urlhandle = UrlHandle()
        self.dirfuzz = DirFuzz()

    def test(self):
        self.dirfuzz.test()