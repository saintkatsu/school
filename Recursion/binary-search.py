Array = [1,2,3,4,5,6,7,8,9]
def BinarySearch(DataToSearch):
    global Array
    lowerbound = 0
    upperbound = len(Array)
    for i in range(len(Array)):
        mid = int((lowerbound+upperbound)/2)
        if Array[mid] == DataToSearch:
            return mid
        elif Array[mid] < DataToSearch:
            upperbound = mid - 1
        else:
            lowerbound = mid + 1
print(BinarySearch(5))
