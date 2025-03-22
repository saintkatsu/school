# global stack = [0] * 10
# global stackPointer = 0
global stack
global stackPointer
stack = [0] * 10
stackPointer = 0

def printStack():
    global stackPointer
    global stack
    print("Elements: ")
    for element in stack:
        print(element)
    print("StackPointer:", stackPointer)

def Push(value):
    global stackPointer
    global stack
    if stackPointer > 9:
        return False
    else:
        stack[stackPointer] = value
        stackPointer += 1
        return True
def Pop():
    global stackPointer
    global stack
    if stackPointer == 0:
        return -1 
    else:
        stackPointer -= 1
        return (stack[stackPointer + 1])

for i in range (0,11):
    status = Push(int(input("Enter the value you want to add:")))
    if status == True:
        print("Data added.")
    else:
        print("Stack is full. Could not add data.")


printStack()
