import os

class FileIO(object):

    def FileReadInList(self,file):
        try:
            templist = []
            with open(file,'r') as f:
                for line in f:
                    templist.append(line.replace('\n',''))
            return templist
        except Exception as e:
            print(e)
            return "Error"

if __name__ == "__main__":
    test = FileIO()
    t = test.FileReadInList('../test.txt')
    print(t)
