# a)
import typing # for type hinting

class Character:
    def __init__(self, Name: str, XCoordinate: int, YCoordinate: int) -> None:
        self.__Name: str = Name
        self.__XCoordinate: int = XCoordinate
        self.__YCoordinate: int = YCoordinate
    
    # b)
    def GetName(self) -> str:
        return self.__Name

    def GetX(self) -> int:
        return self.__XCoordinate

    def GetY(self) -> int:
        return self.__YCoordinate

    # c)
    def ChangePosition(self, XChange: int = 0, YChange: int = 0) -> None:
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange

# d)
Characters: typing.List[Character] = []
NoCharacters: int = 10
try:
    with open("Characters.txt", "r", encoding="utf-8") as _file:
        for i in range(0, NoCharacters):
            Name = _file.readline().strip()
            XCoordinate = int(_file.readline().strip())
            YCoordinate = int(_file.readline().strip())
            Characters.append(
                    Character(
                            Name=Name,
                            XCoordinate=XCoordinate,
                            YCoordinate=YCoordinate
                        )
                )

except (IOError, FileNotFoundError):
    print("File not found!")
except Exception as e:
    print(f"Error: {e}")


# e)
SearchedUserIndex: int = -1
while True:
    UCharName = input("[?] Enter character name: ").strip()
    for i in range(0, 10):
        if UCharName == Characters[i].GetName():
            SearchedUserIndex = i
            break
    else:
        print("Please enter a valid name!")
        continue
    break

# f)
while True:
    ULetter = input("[?] Enter letter to change position [A/W/S/D]: ").lower().strip()
    if ULetter == "a":
        Characters[SearchedUserIndex].ChangePosition(XChange=-1, YChange=0)
        break
    elif ULetter == "w":
        Characters[SearchedUserIndex].ChangePosition(XChange=0, YChange=1)
        break
    elif ULetter == "s":
        Characters[SearchedUserIndex].ChangePosition(XChange=0, YChange=-1)
        break
    elif ULetter == "d":
        Characters[SearchedUserIndex].ChangePosition(XChange=1, YChange=0)
        break
    else:
        print("Please enter a valid letter! [A/W/S/D]")


# g) i)
print(f"{Characters[SearchedUserIndex].GetName()} has changed coordinates to X = {Characters[SearchedUserIndex].GetX()} and Y = {Characters[SearchedUserIndex].GetY()}")


# g) ii
# screenshot












