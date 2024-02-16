import datetime
class Character():
    def __init__(self,namep,birthdatep,piq,speedp):
        self.__CharacterName = namep
        self.__DateOfBirth = birthdatep
        self.__Intelligence = piq
        self.__Speed = speedp

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self,iqp):
        self.__Intelligence = iqp

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        return (2023-self.__DateOfBirth.year)

    

