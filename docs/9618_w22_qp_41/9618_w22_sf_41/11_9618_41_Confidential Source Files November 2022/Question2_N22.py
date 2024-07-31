# a) i)
import typing

class Card:
    def __init__(self, Number: int, Colour: typing.Literal["red", "blue", "yellow"]) -> None:
        if not (1 <= Number <= 5):
            raise ValueError("")
        self.__Number = Number
        self.__Colour = Colour

    # a) ii)
    def GetNumber(self) -> int:
        return self.__Number

    def GetColour(self) -> typing.Literal["red", "blue", "yellow"]:
        return self.__Colour

# a) iii)
OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")

OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")

OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

# b) i)
class Hand:
    def __init__(self, *args: Card) -> None:

        self.__Cards: typing.List[Card] = list(args)[:5]

        # or this, if we don't want to specify the type in *args
        # ---
        # self.__Cards: typing.List[Card]
        # for arg in args: # only append objects of Card
        #    if isinstance(arg, Card):
        #        self.__Cards.append(arg)
                
        self.__FirstCard = 0
        self.__NumberOfCards = len(self.__Cards)

    # b) ii
    def GetCard(self, idx) -> Card:
        return self.__Cards[idx] 

# b) iii)
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)


# c) i)
def CalculateValue(player: Hand) -> int:
    score = 0
    for i in range(0, 5):
        cd = player.GetCard(idx=i)
        score += cd.GetNumber()
        col = cd.GetColour()
        if col  == "red":
            score += 5
        elif col == "blue":
            score += 10
        elif col == "yellow":
            score += 15
    return score

# c) ii)
sp1 = CalculateValue(player=Player1)
sp2 = CalculateValue(player=Player2)
if sp1 == sp2:
    print("It's a draw")
elif sp1 > sp2:
    print(f"Player 1 won by {sp1-sp2} marks.")
else:
    print(f"Player 2 won by {sp2-sp1} marks.")





        
