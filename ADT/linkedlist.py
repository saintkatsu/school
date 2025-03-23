class Node:
    def __init__(self, Data, Pointer):
        self.Data = Data
        self.Pointer = Pointer

LinkedList = [Node(1, 1),Node(5,4), Node(6, 7), Node(7,-1), Node(2,2), Node(0, 6), Node(0, 8),Node(56, 3),Node(0, 9),Node(0, -1)] 

global startPointer
global emptyList
emptyList = 5
startPointer = 0

def addNode(Data):
    global startPointer
    global emptyList

    if emptyList < 0 or emptyList > 9:
        print("LinkedList is full.")

    else:
        freelist = emptyList
        emptyList = LinkedList[emptyList].Pointer
        LinkedList[freelist] = Node(Data, -1)

        currentPointer = startPointer
        previousPointer = 0
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = LinkedList[currentPointer].Pointer
        LinkedList[previousPointer].Pointer = freelist

def printNodes():
    global startPointer
    currentPointer = startPointer
    while currentPointer != -1:
        print(LinkedList[currentPointer].Data)
        currentPointer = LinkedList[currentPointer].Pointer

def deleteNode(Data):
    global startPointer
    global emptyList
    currentPointer = startPointer
    previousPointer = 0
    while currentPointer != -1 and LinkedList[currentPointer].Data != Data:
        previousPointer = currentPointer
        currentPointer = LinkedList[currentPointer].Pointer
    if currentPointer == -1:
        print("Could not find he value.")
    else:
        if currentPointer == 0:
            startPointer = LinkedList[currentPointer].Pointer
        else:
            LinkedList[previousPointer].Pointer = LinkedList[currentPointer].Pointer  
            
        LinkedList[currentPointer].Pointer = emptyList
        LinkedList[currentPointer].Data = 0
        emptyList = currentPointer

def searchValue(value):
    global startPointer
    currentPointer = startPointer
    while currentPointer != -1:
        if LinkedList[currentPointer].Data == value:
            return (currentPointer)
        else:
            currentPointer = LinkedList[currentPointer].Pointer
    return -1
printNodes()
deleteNode(7)
print("After:")
printNodes()
print(searchValue(6))
