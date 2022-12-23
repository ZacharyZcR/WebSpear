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

    def FileWriteInTxt(self,list,file):
        try:
            templist = list
            with open(file,'w') as f:
                for element in templist:
                    f.write(element+'\n')
        except Exception as e:
            print(e)




if __name__ == "__main__":
    test = FileIO()
    t = test.FileReadInList('../test.txt')
    print(t)
