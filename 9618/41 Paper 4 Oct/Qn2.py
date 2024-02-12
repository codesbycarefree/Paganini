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
    try:
        Filename = "Pictures.txt"
        File = open(Filename,'r')
        
    except IOError:
        print("Couldn't find the file.")
    return Picturearray
