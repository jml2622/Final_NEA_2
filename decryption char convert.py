plaintext= []

class encryption():
    def __init__(self):
        self.array = ['E', ',','P', ',', 'H', ',', 'H', ',', 'K', ',', 'M', ',', 'W', ',', '&', ',', 'E', ',', 'P', ',', 'H', ',', 'H', ',', '&', ',', 'W', ',', 'M', ',', 'K', ',']
        self.pos1 = 0
        self.pos2 = 1
        self.string = []
    def ConverttoAscii(self):
        for i in range(0,len(self.array)):
            temp = self.array[i]
              #if temp == ',':
                   #pass
              #else:
            print(temp)
            temp = ord(temp)
            self.string.append(temp)
            print(self.string)
        for d in range(0,len(self.string)):
            while d > len(self.string)+1:
                d = d + 1
                del self.string[d]

    def PosEdit(self):
        for n in range (1,len(self.string)):
            if self.pos2 < len(self.string):
                self.string[self.pos1] = self.string[self.pos1] - self.pos2+1
                self.string[self.pos2] = self.string[self.pos2] - self.pos1+1
                self.pos1 +=1
                self.pos2 +=1
                print(self.pos1)
                print(self.pos2)
                print(self.string)
            elif self.pos2 == len(self.string):
                    Save()
    def Save(self):
        for c in range(0,len(self.string)):
                plaintext.append(chr(self.string[c]))
                print(plaintext)
                       
# e = encryption()
# e.ConverttoAscii()
# e.PosEdit()
# e.Save()
