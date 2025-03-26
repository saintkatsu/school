def InsertionSort():
    Array = [2,6,5,1,3,4]
    NumberItems = len(Array)
    for i in range(1, NumberItems):
        j = i
        while Array[j - 1]> Array[j] and j > 0:
            Array[j - 1], Array[j] = Array[j], Array[j - 1]
            j -= 1
    print(Array)
InsertionSort()
