def LinearSearch(target,Array):
    for i in range(len(Array)):
        if Array[i]==target:
            return i

Array1 = [22,11,69,33,6,12]
Index = LinearSearch(6,Array1)
print(Index)