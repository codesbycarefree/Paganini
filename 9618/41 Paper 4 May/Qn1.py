class node():
    def __init__(self,datanew,numnextNode):
        self.data = datanew
        self.nextNode = numnextNode

    def outputNodes(self,startPointer):
        while startPointer != -1:
            print(str(linkedList[startPointer].data))
            startPointer = linkedList[startPointer].nextNode

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer =0
emptyList = 5
