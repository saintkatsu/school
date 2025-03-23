global Names 
global HeadPointer
global TailPointer
Names = [""] * 6
HeadPointer = -1 
TailPointer = 0

def Enqueue(value): 
    global Names 
    global HeadPointer
    global TailPointer
    if TailPointer > 5:
        print("Queue Full.")
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        Names[TailPointer] = value
        TailPointer += 1
def Dequeue():
    global Names 
    global HeadPointer
    global TailPointer
    if HeadPointer == -1:
        print("Queue is empty.")
    else:
       TailPointer -= 1 

    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0
