import datetime


# a) i)
class Character:
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
        # self.__CharacterName string
        # self.__DateOfBirth date
        # self.__Intelligence real
        # self.__Speed integer
        self.__CharacterName = CharacterName
        self.__DateOfBirth = DateOfBirth
        self.__Intelligence = Intelligence
        self.__Speed = Speed

    # a) ii)
    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    # a) iii)
    def SetIntelligence(self, value):
        self.__Intelligence = value

    # a) iv)
    def Learn(self):
        self.__Intelligence *= 1.1

    # a) v)
    def ReturnAge(self):
        current_year = datetime.datetime.now().year
        return current_year - self.__DateOfBirth.year


# b) i)
FirstCharacter = Character(
    CharacterName="Royal",
    DateOfBirth=datetime.datetime(
        2019,
        1,
        1,
    ),
    Intelligence=70,
    Speed=30,
)

# b) ii)
FirstCharacter.Learn()
print(
    f"{FirstCharacter.GetName()} is {FirstCharacter.ReturnAge()} years old with an intelligence of {FirstCharacter.GetIntelligence()}"
)

# b) iii) screenshot


# c)
class MagicCharacter(Character):
    def __init__(self, Element, CharacterName, DateOfBirth, Intelligence, Speed):
        # self.__Element string

        super().__init__(
            CharacterName=CharacterName,
            DateOfBirth=DateOfBirth,
            Intelligence=Intelligence,
            Speed=Speed,
        )
        self.__Element = Element

    #
    def Learn(self):
        if (self.__Element == "fire") or (self.__Element == "water"):
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif self.__Element == "eart":
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)


# d) i)
FirstMagic = MagicCharacter(
    Element="fire",
    CharacterName="Light",
    DateOfBirth=datetime.datetime(2018, 3, 3),
    Intelligence=75,
    Speed=22,
)
FirstMagic.Learn()
print(
    f"{FirstMagic.GetName()} is {FirstMagic.ReturnAge()} years old with an intelligence of {FirstMagic.GetIntelligence()}"
)
