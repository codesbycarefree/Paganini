class character():
    def __init__(self,name,xcord,ycord):
        self.Name = name
        self.XCoordinate = xcord
        self.YCoordinate = ycord

    def GetName(self):
        return self.Name

    def GetX(self):
        return self.XCoordinate

    def GetY(self):
        return self.YCoordinate

    def ChangePosition(self,XChange,YChange):
        self.XCoordinate = self.XCoordinate + XChange
        self.YCoordinate = self.YCoordinate + YChange

filename = "/Characters.txt"
ArrayCharacter=[""]*30
x=open(filename,'r')
for i in range(0,10):
    ArrayCharacter[i] = x.readline()
    ArrayCharacter[i+1]= x.readline()
    ArrayCharacter[i+2] = x.readline()
x.close()

searchname = input("enter search name:")

for j in range(0,30):
    if ArrayCharacter[j]==searchname:
        foundindex = j






