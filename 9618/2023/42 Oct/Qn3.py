import datetime
class Character():
    def __init__(self,namep,birthdatep,piq,speedp):
        self.__CharacterName = namep #string
        self.__DateOfBirth = birthdatep #date
        self.__Intelligence = piq #integer
        self.__Speed = speedp #integer

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


FirstCharacter = Character("Royal",datetime.datetime(2019,1,1),70,30)
FirstCharacter.Learn()
print("The character's name is",str(FirstCharacter.GetName())+", his age is",FirstCharacter.ReturnAge(),"and has intelligence",str(FirstCharacter.GetIntelligence())+".")

class MagicCharacter(Character):
    def __init__(self,elementp,namep,birthdatep,piq,speedp,):
        self.__Element = elementp #string
        super().__init__(self,namep,birthdatep,piq,speedp)

    def Learn(self):
        if str(self.__Element).lower() == "fire" or "water":
            super().SetIntelligence(super().GetIntelligence()*1.2)
        elif str(self.__Element).lower() == "earth":
            super().SetIntelligence(super().GetIntelligence()*1.3)
        else:
            super().SetIntelligence(super().GetIntelligence()*1.1)

FirstMagicCharacter = MagicCharacter("fire","Light",datetime.datetime(2018,3,3),75,22)
FirstMagicCharacter.Learn()
print("The character's name is",str(FirstMagicCharacter.GetName())+", his age is",FirstMagicCharacter.ReturnAge(),"and has intelligence",str(FirstMagicCharacter.GetIntelligence())+".")
