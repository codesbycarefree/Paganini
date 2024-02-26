class node():
    def __init__(self,datanew,numnextNode):
        self.data = datanew
        self.nextNode = numnextNode

    def outputNodes(self,startPointer):
        while startPointer != -1:
            print(str(linkedList[startPointer].data))
            startPointer = linkedList[startPointer].nextNode

    def addNode(self,linkedList,startPointer,emptyList):
        datatoadd = int(input("Enter the data to be added:"))
        if emptyList > 9 or emptyList < 0:
            return False
        else:
            newNode = node(int(datatoadd,-1))
            linkedList[emptyList]= newNode
            emptyList = linkedList[emptyList].nextNode
            previouspointer =  0
            while startPointer != -1:
                previouspointer=startPointer
                linkedList[startPointer].nextnode = emptyList
                emptylist = linkedList
linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer =0
emptyList = 5
x = node.outputNodes(linkedList,startPointer)
