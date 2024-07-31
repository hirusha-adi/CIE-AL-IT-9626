---
title: "9618_w22_qp_41 (2022 Nov 41)"
sidebar_label: "9618_w22_qp_41"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_w22_qp_41.pdf)
- [Exam Resources](./9618_w22_sf_41.zip)
- [My Answers `(evidence.doc)`](./9618_w22_sf_41/11_9618_41_Confidential%20Source%20Files%20November%202022/evidence.doc)

</details>

## Question 1

```python

# a)
DataArray = [] # 100 integers

# b)
def ReadFile() -> None:
    global DataArray
    try:
        with open("IntegerData.txt", "r", encoding="utf-8") as _file:
            for line in _file.readlines():
                try:
                    DataArray.append(int(line.strip()))
                except ValueError:
                    print(f"{line.strip()} is not an integer in the text file. Skipping...")
    except (IOError, FileNotFoundError):
        print("File not found!")
    except Exception as e:
        print(f"Error: {e}")


# c)
def FindValues() -> int:
    global DataArray
    while True:
        value = input("[?] Enter a value to search for: ").strip().replace("_", "")
        try:
            if "." in value: # prevent the user from entering floats (decimal numbers)
                raise ValueError
            value = int(value)
            break
        except ValueError:
            print("Please enter a valid integer!")
        except Exception as e:
            print(f"Error: {e}")
    count = 0
    for el in DataArray:
        if value == el:
            count += 1
    
    return count
    
# d) i)
ReadFile()
count = FindValues()
print(f"The number was found {count} times")

# d) ii)
# screenshot

# e)
def BubbleSort():
    global DataArray
    n = len(DataArray)
    for i in range (n-1):
        for j in range(0, n-i-1):
            if DataArray[j] > DataArray[j+1]:
                DataArray[j], DataArray[j+1] = DataArray[j+1], DataArray[j]

BubbleSort()
print(DataArray)
```

## Question 2

```python
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
```

## Question 3

```python
# a)
# ArrayNodes = [[-1, -1, -1]] * 20

# b)
ArrayNodes = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1]]
FreeNodes = 6
RootPointer = 0


# c)
def SearchValue(Root, ValueToFind):
    global ArrayNodes
    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)


# d) PLEASE LEARN THIS
# I HAVE NO CLUE
# PASTED BELOW IS THE ANSWER FROM THE MARKING SCHEME
def PostOrder(RootNode):
    if RootNode[0] != -1:
        PostOrder(ArrayNodes[RootNode[0]])
    if RootNode[2] != -1:
        PostOrder(ArrayNodes[RootNode[2]])
    print(str(RootNode[1]))


# e) i)
ReturnValue = SearchValue(RootPointer, 15)
if ReturnValue == -1:
    print("Not found")
else:
    print("Found at " + str(ReturnValue))
PostOrder(ArrayNodes[RootPointer])
```

