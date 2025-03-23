# DECALRE NumberOfItems : Integer
# DECLARE HeadPointer : Integer
# DECLARE QueueArray: ARRAAY [0:9] OF STRING
# DECLARE TailPointer: Integer
global NumberItems
global HeadPointer
global TailPointer
NumberItems = 0
HeadPointer = 0
TailPointer = 0
QueueArray = [""] * 10

def Enqueue(DataToAdd):
    global NumberItems
    global HeadPointer
    global TailPointer
    if NumberItems == 10:
        return False
    else:
        QueueArray[TailPointer] = DataToAdd
        if TailPointer >= 9:
            TailPointer = 0
        else:
            TailPointer= TailPointer + 1
        NumberItems += 1
        return True

def Dequeue():
    global NumberItems
    global HeadPointer
    global TailPointer
    if NumberItems == 0:
        return -1
    else:
        temp = QueueArray[HeadPointer]
        NumberItems -= 1
        if HeadPointer >= 9:
            HeadPointer = 0
        else:
            HeadPointer += 1
        return temp

Enqueue("Pranav")
Enqueue("Ram")
Enqueue("Sabina")
Enqueue("Alok")
Enqueue("Katsu")
Enqueue("Shyam")
Enqueue("Hari")
Enqueue("Krishna")
Enqueue("Sita")
Enqueue("Geeta")
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(QueueArray)
print(NumberItems)
