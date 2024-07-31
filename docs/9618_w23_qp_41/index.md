---
title: "9618_w23_qp_41 (2023 Nov 41)"
sidebar_label: "9618_w23_qp_41"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_w23_qp_41.pdf)
- [Exam Resources](./9618_w23_sf_41.zip)
- [My Answers `(evidence.doc)`](./9618_w23_sf_41/11_9618_41_SourceFiles/evidence.doc)

</details>

## Question 1

```python
# a) i)
def IterativeVowels(Value):
    # Value string
    # IterateVowels() returns integer
    Total = 0
    for x in range(0, len(Value)):
        FirstCharacter = Value[0].lower()
        if FirstCharacter in ["a", "e", "i", "o", "u"]:
            Total += 1
        Value = Value[1:len(Value)]
    return Total

# a) ii)
print(IterativeVowels("house"))

# b) i)
def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    else:
        fch = Value[0]
    if fch in ["a", "e", "i", "o", "u"]:
        return 1 + RecursiveVowels(Value[1:len(Value)])
    else:
        return RecursiveVowels(Value[1:len(Value)])
    
# b) ii
print(RecursiveVowels("imagine"))
```

## Question 2

- I have so many doubts about this. Not even the code given in the marking scheme provides the output given in the marking scheme itself. 

### My Answer

```python
# a) i)
Queue = []  # 50 ineteger
HeadPointer = -1  # integer
TailPointer = 0  # integer


# a) ii)
def Enqueue(value):
    global Queue, HeadPointer, TailPointer
    if TailPointer == 50:
        print("Queue is full")
    else:
        Queue.append(value)
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0


# a) iii)
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if (HeadPointer == -1) or (HeadPointer == TailPointer):
        print("Empty Queue")
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer - 1]


# b)
def ReadData():
    try:
        with open("QueueData.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                Enqueue(value=line.strip())
    except IOError:
        print("File not found")
    except Exception as e:
        print(f"Another error occured: {e}")


# c) i)
class RecordData:
    # self.ID string
    # self.Total integer
    def __init__(self, ID=None, Total=None):
        self.ID = ID
        self.Total = Total


# c) ii
Records = []  # 50 elements of type RecordData
# Records = [RecordData(ID=None, Total=None)] * 50  # 50 elements of type RecordData
NumberRecords = 0  # integer


# c) iii)
def TotalData():
    global NumberRecords, Records

    Flag = False
    DataAccessed = Dequeue()

    if NumberRecords == 0:
        Records.append(RecordData(ID=DataAccessed, Total=1))
        Flag = True
        NumberRecords += 1
    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total += 1
                Flag = True
        if Flag is False:
            Records.append(RecordData(ID=DataAccessed, Total=1))
            NumberRecords += 1


def OutputRecords():
    already_printed = []
    for x in range(0, NumberRecords):
        record = Records[x]
        if not ((record.ID == "") or (record.Total == 0)):
            if not (record.ID in already_printed):
                print(f"ID {record.ID} Total {record.Total}")
                already_printed.append(record.ID)
    print(already_printed)


ReadData()
# PLEASE REMEMBER THIS PART! PLEASE!!!
while HeadPointer != TailPointer:
    TotalData()
    OutputRecords()

```

### Marking Scheme

```python
# a) i)
# main
Queue = []  # string 50 elements
HeadPointer = -1
TailPointer = 0


def Enqueue(Data):
    global TailPointer
    global HeadPointer
    global Queue
    if TailPointer == 50:
        print("Queue full")
    else:
        Queue.append(Data)
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0


# a) iii)
def Dequeue():
    global Queue
    global HeadPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue empty")
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer - 1]


# b)
def ReadData():
    try:
        DataFile = open("QueueData.txt")
        for Line in DataFile:
            Enqueue(Line.strip())
        DataFile.close()
    except IOError:
        print("No file")


# c) i)
class RecordData:
    # self.ID string
    # self.Total integer
    def __init__(self, ID, Total):
        self.__ID = ID
        self.__Total = Total

    def SetID(self, Value):
        self.__ID = Value

    def GetID(self):
        return self.__ID

    def SetTotal(self, Value):
        self.__Total = Value

    def GetTotal(self):
        return self.__Total


# c) ii
Records = []  # 50 elements of type RecordData
NumberRecords = 0  # integer


# c) iii)
def TotalData():
    global NumberRecords
    global Records
    Flag = False
    DataAccessed = Dequeue()
    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1
        Flag = True
    else:
        for X in range(0, NumberRecords):
            if Records[X].GetID() == DataAccessed:
                Records[X].SetTotal(Records[X].GetTotal() + 1)
                Flag = True
    if Flag == False:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1


# d)
def OutputRecords():
    for X in range(0, NumberRecords):
        print("ID", Records[X].GetID(), " Total ", Records[X].GetTotal())


# e) i
Records = []
HeadPointer = 0
TailPointer = 0
ReadData()
NumberRecords = 0
while HeadPointer != TailPointer:
    TotalData()
    OutputRecords()

```

## Question 3

```python
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

```

