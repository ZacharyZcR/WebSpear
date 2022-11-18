import os

dir = os.listdir('./module')
# print(dir)
for model in dir:
    print(model)
    __import__('module.' + model[:-3])

# HttpConfig()
# a.test()
