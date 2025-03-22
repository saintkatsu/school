global stack
global stackPointer
stackPointer = -1
stack = [""] * 5
def push(passenger):
    global stack
    global stackPointer 
    if stackPointer == 4: 
        print("Stack is full")
    else:
        stackPointer += 1
        stack[stackPointer] = passenger


def pop():
    global stackPointer
    global stack
    if stackPointer == -1:
        print("Stack is empty.")
    else:
        stackPointer = stackPointer - 1
        stack[stackPointer] = ""

push("Shrijana")
push("Pranav")
push("Kalin")
print(stack)
pop()
print(stack)
