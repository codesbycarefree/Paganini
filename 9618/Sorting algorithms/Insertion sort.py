Array = [12,11,13,5,6]

def InsertionSort(Array):
    for i in range(1,len(Array)):
        key = Array[i]

        j=i-1
        while j >=0 and key < Array[i]:
            Array[j+1]=Array[j]
            j -= 1
        Array[j+1] = key

    print(Array)



print(Array)
print("Sorted Array")
