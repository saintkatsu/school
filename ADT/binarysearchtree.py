from re import A


global ArrayNodes
global RootPointer
global FreeNode
ArrayNodes = [[0]*3 for i in range (20)]
RootPointer = -1
FreeNode = 0

def AddNode(value):
    global ArrayNodes
    global RootPointer
    global FreeNode
    
    if FreeNode < 0 and FreeNode > 19:
        return False #Binary Tree is full
    else:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = value
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            curretPointer = RootPointer
            placed = False
            while placed == False:
                if value < ArrayNodes[curretPointer][1]:
                    if ArrayNodes[curretPointer][0] == -1:
                        ArrayNodes[curretPointer][0] = FreeNode
                        placed = True
                    else:
                        curretPointer = ArrayNodes[curretPointer][0]
                else:
                    if ArrayNodes[curretPointer][2] == -1:
                        ArrayNodes[curretPointer][2] = FreeNode
                        placed = True
                    else:
                        curretPointer = ArrayNodes[curretPointer][2]                

        FreeNode += 1

def searchNodes(value):
    global RootPointer
    global FreeNode
    global ArrayNodes
    
    currentPointer = RootPointer
    while currentPointer != -1 and value != ArrayNodes[currentPointer][1]:
        if ArrayNodes[currentPointer][1] < value:
            currentPointer = ArrayNodes[currentPointer][2]
        else:
            currentPointer = ArrayNodes[currentPointer][0]
    if currentPointer == -1:
        return -1
    else:
        return currentPointer

AddNode(10)
AddNode(30)
AddNode(9)
AddNode(25)
AddNode(8)
AddNode(40)
AddNode(4)
AddNode(50)
print(searchNodes(9))
print(ArrayNodes)
