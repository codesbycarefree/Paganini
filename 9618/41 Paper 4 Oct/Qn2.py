class Picture():
    def __init__(self,Pdescription,Pwidth,Pheight,Pframecolour):
        self.__Description=Pdescription
        self.__Width = Pwidth
        self.__Height = Pheight
        self.__FrameColour = Pframecolour

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self,descriptiontoadd):
        self.__Description = descriptiontoadd


def ReadData():
    index =0
    Picturearray = [0]*100
    for i in range(100)
        Picturearray.append(Picture("",0,0,""))

    try:
        Filename = "Pictures.txt"
        File = open(Filename,'r')
        Description = File.readline().rstrip()
        while Description != "":
            Width = int(File.readline())
            Height = int(File.readline())
            Framecolour = File.readline().rstrip()
            Picturearray[index]= Picture(Description,Width,Height,Framecolour)
            Description = File.readline().rstrip()
            index =+1
    except IOError:
        print("Couldn't find the file.")
    return Picturearray

