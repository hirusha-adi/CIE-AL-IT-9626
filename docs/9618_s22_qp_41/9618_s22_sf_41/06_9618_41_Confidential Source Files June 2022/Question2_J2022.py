# a)
class Balloon:
    #Health as integer
    #Colour as string
    #DefenceItem as string
    def __init__(self, DefenceItem: str, BalloonColor: str) -> None:
        self.__Health: int = 100
        self.__DefenceItem: str = DefenceItem
        self.__BaloonColor: str = BalloonColor

    # b)
    def GetDefenceItem(self) -> str:
        return self.__DefenceItem

    # c)
    def ChangeHealth(self, value: int) -> None:
        self.__Health += value

    # d)
    def CheckHealth(self) -> bool:
        if self.__Health <= 0:
            return True
        return False
# e)
DefenceItem = input("? Enter Defence Item: ").strip()
BalloonColor = input("? Enter Ballon Color: ").strip()
Balloon1 = Balloon(DefenceItem=DefenceItem, BalloonColor=BalloonColor)

# f)
def Defend(obj: Balloon) -> Balloon:
    while True:
        try:
            inp_strength = int(input("? Enter strength of opponent: ").strip())
            break
        except ValueError:
            print("Please enter a valid integer")
        except Exception as e:
            print(f"Another error has occured: {e}")
    obj.ChangeHealth(-inp_strength)
    print(f"You defended with {obj.GetDefenceItem()}")
    if obj.CheckHealth() == True:
        print("Defence Failed")
    else:
        print("Defence Succeeded")
    return obj

# g) i)
Defend(obj=Balloon1)

# g) ii)
# screenshot

