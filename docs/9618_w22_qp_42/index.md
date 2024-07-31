---
title: "9618_w22_qp_42 (2022 Nov 42)"
sidebar_label: "9618_w22_qp_42"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_w22_qp_42.pdf)
- [Exam Resources](./9618_w22_sf_42.zip)
- [My Answers `(evidence.doc)`](./9618_w22_sf_42/11_9618_42_Confidential%20Source%20Files%20November%202022/evidence.doc)

</details>

## Question 1

```python

# a)
Jobs = [] # global 2 dimentional array of type integer, 100 by 2 elements
NumberOfJobs = 0 # global integer

# b)
def Initialise():
    global Jobs
    global NumberOfJobs
    for i in range(0, 100):
        Jobs.append([-1, -1])
    NumberOfJobs = 0

# c)
def AddJob(JobNumber, Priority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs == 100:
        print("Not added") # our array is full
    else:
        Jobs[NumberOfJobs] = [JobNumber, Priority]
        print("Added")
        NumberOfJobs += 1

# d)
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

# e)
# PLEASE TAKE A LOOK AT THIS AGAIN
# since i have no idea about this, in the exam,
# use something like .sort() and continue to get marks for the others
# and also the final mark for the screen shot
def InsertionSort():
     global Jobs
     global NumberOfJobs
     for I in range(1, NumberOfJobs):
         Current1 = Jobs[I][0]
         Current2 = Jobs[I][1]
         while I > 0 and Jobs[I-1][1] > Current2:
             Jobs[I][0] = Jobs[I-1][0]
             Jobs[I][1] = Jobs[I-1][1]
             I = I - 1
         Jobs[I][0] = Current1
         Jobs[I][1] = Current2
# marks are given as follows:
# Procedure header (and end where appropriate)
# • Outer loop through all 5 elements / number of jobs …
# • … inner loop through array elements …
# • …and comparing priority (second index) …
# • …moving the elements up and inserting correctly


# f)
def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(0, NumberOfJobs):
        element = Jobs[i]
        print(f"{element[0]} priority {element[1]}")

# g) i)
InsertionSort()
PrintArray()

```

## Question 2

```python
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

```

## Question 3

```python
# a)
Queue = [-1]*100 # integer
HeadPointer = -1 # integer
TailPointer = 0 # integer

# b) PLEASE REMEBER THIS FOR THE EXAM
def Enqueue(value) -> bool:
    global Queue, HeadPointer, TailPointer
    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = value
        TailPointer = TailPointer + 1
        return True
    return False

# c)
for num in range(1, 21):
    status = Enqueue(value=num)
if status:
    print("Successful")
else:
    print("Unsuccessful")

# d)
def ResucrsiveOutput(start: int) -> int:
    global Queue
    
    # base condition
    if start == 0:
        return Queue[start]
    # recursive condition
    else:
        return Queue[start] + ResucrsiveOutput(start-1)

# e) i)
print(ResucrsiveOutput(TailPointer-1))


```

