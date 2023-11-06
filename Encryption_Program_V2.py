import subprocess
from client_2 import run as  run_client
import os

Ascii = []

CompleteAscii = []

def AsciiChange():
    def __init__(self):
        #file = open("new message.txt", "r")
        #self.string = file.read()
        self.string = ("CODE RED")
        self.pos1 = 0
        self.pos2 = 1
    def AsciiConvert(self,):
        for x in range(0, len(self.string)):
            temp = ord(self.string[x])
            Ascii.append(temp)
            print(Ascii)

    def PosEdit(self):
        for n in range (1,len(self.string)):
            if self.pos2 < len(self.string):
                Ascii[self.pos1] = Ascii[self.pos1] + self.pos2+1
                Ascii[self.pos2] = Ascii[self.pos2] + self.pos1+1
                self.pos1 +=2
                self.pos2 +=2
                print(self.pos1)
                print(self.pos2)
                print(Ascii)
            elif self.pos2 == len(self.string):
                pass
    def Save(self):
        for c in range(0,len(self.string)):
                CompleteAscii.append(chr(Ascii[c]))
                print(CompleteAscii)

class Node:
    def __init__(self,d,l, p = None):
        self.data = d
        self.parent = p 
        self.left = None
        self.right = None
        self.level = 1

    def __str__(self):
        return self.data
    
def construct_tree(array, node):
    
    o_queue = [] 

    o_queue.append(node)

    while o_queue != []:

        current = o_queue.pop(0)

        if len(array) >=2:
           
            current.left = Node(array.pop(0), current.level + 1, current)
            current.right =Node(array.pop(0), current.level +1, current)

            o_queue.append(current.left)
            o_queue.append(current.right)

        elif len(array) == 1:
            current.left = Node(array.pop(0),current.level+1, current)
            o_queue.append(current.left)
        else:
            return
def read_tree(node, array, completecypher):
    o_queue = []

    o_queue.append(node)

    while o_queue != []:
        try:
            current = o_queue.pop(0)

            completecypher.append(current.data)

            o_queue.append(current.right)
            print(current.right)
            o_queue.append(current.left)
            print(current.left)
        except:
            break
   

        while o_queue != []:
            try:
                current = o_queue.pop(0)

                completecypher.append(current.data)

                o_queue.append(current.right)
                print(current.right)
                o_queue.append(current.left)
                print(current.left)
            except:
                break
            while o_queue != []:
                try:
                    current = o_queue.pop(0)

                    completecypher.append(current.data)

                    o_queue.append(current.right)
                    print(current.right)
                    o_queue.append(current.left)
                    print(current.left)
                except:
                    break
            return


def complete(node, array, completecypher):  
 
    o_queue = []

    o_queue.append(node)
    while o_queue != []:
        try:
            current = o_queue.pop(0)

            completecypher.append(current.data)

            o_queue.append(current.left)
            print(current.left)
            o_queue.append(current.right)
            print(current.right)
        except:
            break




    

    
def main():
    array=[]
    for n in range(0,len(CompleteAscii)):
        array.append( CompleteAscii[n])
        array.append(",")
    print(array)
    root = Node(array.pop(0), 1)
    completecypher  = [] 
    construct_tree(array,root)

    string_array = []

    read_tree(root, string_array, completecypher)
    complete(root, string_array, completecypher)
    print("cypher compiled")
    #str(completecypher).encode(encoding ='UTF-8',errors = 'strict')
    completecypher = ''.join(completecypher)
    completecypher = completecypher.encode()
    #os.chdir()
    file = open("cypher.txt","wb")

    file.write(completecypher)
    file.close()
    
    run_client()
    exit()
    

                       
# e = AsciiChange()
# e.AsciiConvert()
# e.PosEdit()
# e.Save()
# main()
