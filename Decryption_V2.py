import os

class Translation:
    global array 
    array = []
    count=0
    file = open("cypher.txt", "rb")
    cyphertext = file.read().decode()
    print(cyphertext)
    print(len(cyphertext))
    file.close()
    for n in range(0,len(cyphertext)):
        print(count)
        word = cyphertext[count]
        array.append(word)
        count+=1
    print(array)


class Node:

    def __init__(self,key):
        self.data = key
        self.left = None 
        self.right = None 

def printtraverse(root):
    h = height(root)
    for n in range(1, h+1):
        currentlev(root, n)

def currentlev(root, level):
    if root is None:
        return("empty")
    if level == 1:
        print(root.data, end="")
    elif level > 1:
        currentlev(root.left, level-1)
        currentlev(root.right, level=1)

def height(node):
    if node is None:
        return 0
    else:
        lefheight = height(node.left)
        riheight = height(node.left)

        if lefheight > riheight:
            return lefheight+1 
        else:
            return riheight+1
        
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
    


def run():
    array = []
    count = 0
    file = open("cypher.txt", "rb")
    cyphertext = file.read().decode()
    file.close()
    for n in range(0,len(cyphertext)):
        while count <= len(cyphertext):
            word = cyphertext[count]
            array.append(word)
            count+=2
    print(array)


    print("level order =")
    printtraverse()