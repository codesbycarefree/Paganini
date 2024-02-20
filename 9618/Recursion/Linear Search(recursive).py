x=0
def RecursiveSearch(Array,target,x):
    if x>len(Array):
        return ("Not found")

    if target == Array[x]:
        return x
    else:
        RecursiveSearch(Array,target,x+1)