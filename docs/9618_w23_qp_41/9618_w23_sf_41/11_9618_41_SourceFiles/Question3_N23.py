import typing


# a) i)
class Character:
    # self.__Name string
    # self.__XPosition integer
    # self.__YPosition integer

    def __init__(self, Name: str, XPosition: int, YPosition: int) -> None:
        self.__Name: str = Name
        self.__XPosition: int = XPosition
        self.__YPosition: int = YPosition

    def __repr__(self):
        return f"<Character Name={self.__Name} XPosition={self.__XPosition} YPosition={self.__YPosition}>"

    # a) ii)
    def GetName(self) -> str:
        return self.__Name

    def GetXPosition(self) -> int:
        return self.__XPosition

    def GetYPosition(self) -> int:
        return self.__YPosition

    # a) iii)
    def SetXPosition(self, value: int) -> None:
        self.__XPosition += value
        if self.__XPosition > 10_000:
            self.__XPosition = 10_000
        if self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, value: int) -> None:
        self.__YPosition += value
        if self.__YPosition > 10_000:
            self.__YPosition = 10_000
        if self.__YPosition < 0:
            self.__YPosition = 0

    # a) iv)
    def Move(self, direction: typing.Literal["up", "down", "left", "right"]) -> None:
        if direction == "up":
            self.SetYPosition(10)
        elif direction == "down":
            self.SetYPosition(-10)
        elif direction == "left":
            self.SetXPosition(-10)
        elif direction == "right":
            self.SetXPosition(10)


# b)
Jack = Character(Name="Jack", XPosition=50, YPosition=50)


# c) i)
class BikeCharacter(Character):
    def __init__(self, Name: str, XPosition: int, YPosition: int) -> None:
        super().__init__(Name=Name, XPosition=XPosition, YPosition=YPosition)

    def __repr__(self):
        return f"<BikeCharacter Name={self.__Name} XPosition={self.__XPosition} YPosition={self.__YPosition}>"

    # c) ii)
    def Move(self, direction: typing.Literal["up", "down", "left", "right"]) -> None:
        if direction == "up":
            self.SetYPosition(20)
        elif direction == "down":
            self.SetYPosition(-20)
        elif direction == "left":
            self.SetXPosition(-20)
        elif direction == "right":
            self.SetXPosition(20)


# d)
Karla = BikeCharacter(Name="Karla", XPosition=100, YPosition=50)


# e) i)

person: typing.Union[Character, BikeCharacter]

while True:
    move_character = (
        input("[?] Which character do you want to move [jack/karla]: ").strip().lower()
    )
    if move_character == "jack":
        person = Jack
        break
    elif move_character == "karla":
        person = Karla
        break
    else:
        print("Please enter a valid input!")

while True:
    what_direction = (
        input("[?] What direction do you want to move [up/down/left/right]: ")
        .strip()
        .lower()
    )
    if what_direction in ("up", "down", "left", "right"):
        break

person.Move(what_direction)
print(
    f"{person.GetName()}'s new position is X = {person.GetXPosition()} Y = {person.GetYPosition()}"
)
