def InOrder(ArrayNodes, RootPointer):
    if RootPointer == -1:
        return
    if ArrayNodes[RootPointer][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootPointer][0])
    print(ArrayNodes[RootPointer][1]) #IF PREORDER put this line after 1st condition, if post order put it after final condition
    if ArrayNodes[RootPointer][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootPointer][2])
