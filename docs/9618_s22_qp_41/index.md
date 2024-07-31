---
title: "9618_s22_qp_41 (2022 May 41)"
sidebar_label: "9618_s22_qp_41"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_s22_qp_41.pdf)
- [Exam Resources](./9618_s22_sf_41.zip)
- [My Answers `(evidence.doc)`](./9618_s22_sf_41/06_9618_41_Confidential%20Source%20Files%20June%202022/evidence.doc)

</details>

## Question 1

```python
# a)
class Player:
    def __init__(self, name, score: int):
        self.__name = name
        self.__score = score

    def __repr__(self):
        return f"<Player name='{self.__name}' score={self.__score}>"

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def set_score(self, value):
        self.__score = value

PlayerData = []

# b)
def ReadHighScores():
    try:
        with open("HighScore.txt", "r", encoding="utf-8") as file:
            for i in range(10):
                name = file.readline().strip()[:3]
                try:
                    score = int(file.readline().strip())
                except ValueError:
                    print(f"Not an integer after {name}")
                PlayerData.append(Player(name=name, score=score))
    except (IOError, FileNotFoundError):
        print("File not found!")
    except Exception as e:
        print(f"Another errror occured: {e}")

# c) 
def OutputHighScores():
    for element in PlayerData:
        print(f"{element.name} {element.score}")
    
# d) i)
ReadHighScores()
OutputHighScores()

# d) ii)
# screenshot


# e) i)
while True:
    inp_name = input("?) Enter the player name: ").strip().upper()
    if len(inp_name) == 3:
        break

while True:
    inp_score = input("? Enter the player score: ").strip()
    try:
        if "." in inp_score:
            raise ValueError
        inp_score = int(inp_score)
        if (inp_score < 1) or (inp_score > 10000):
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid integer belonging to the given range!")
    except Exception as e:
        print(f"An other error occured: {e}")

# e) ii)
def Foo(name, score):
    last_item = PlayerData[-1]
    if inp_score > last_item.score:
        del PlayerData[-1]
        PlayerData.append(Player(name=name, score=score))
    else:
        print("Player doesn't belong to Top 10")

    n = len(PlayerData)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if PlayerData[j].score < PlayerData[j+1].score:
                PlayerData[j], PlayerData[j+1] = PlayerData[j+1], PlayerData[j]

# e) ii)
Foo(name=inp_name, score=inp_score)
OutputHighScores()

# f)
def WriteTopTen():
    with open("NewHighScore.txt", "w+", encoding='utf-8') as file:
        file.write(f"{PlayerData[0].name}\n{PlayerData[0].score}") # to fix the new line issue
        for el in PlayerData[1:]:
            file.write(f"\n{el.name}\n{el.score}")

WriteTopTen()
```

## Question 2

```python
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
```

## Question 3 - INCOMPLETE

- NOT COMPLETED!!!

```python
QueueArray = [""] * 10

pHead = 0
pTail = 0
noItems = 0

def Enqueue(DataToAdd) -> bool:
    global QueueArray, pHead, pTail, noItems
    if noItems == 10:
        return False
    QueueArray[pTail] = DataToAdd
    if pTail >= 9:
        pTail = 0
    else:
        pTail += 1
    noItems += 1
    return True
```
