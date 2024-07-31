---
title: "9618_s21_qp_42 (2021 May 42)"
sidebar_label: "9618_s21_qp_42"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_s21_qp_42/9618_s21_qp_42.pdf)
- [Exam Resources](./9618_s21_qp_42/9618_s21_sf_42.zip)
- [My Answers `(evidence.doc)`](./9618_s21_qp_42/06_9618_42_Confidential%20Source%20Files%20June%202021/06_9618_42_Confidential%20Source%20Files%20June%202021/evidence.doc)

</details>

## Question 1

```python
# a)
class Node:
    def __init__(self, data: int, nextNode: int) -> None:
        self.data = data
        self.nextNode = nextNode

    def __repr__(self):
        return f"<Node data={self.data} nextNode={self.nextNode}>"

# b)
startPointer = 0
emptyList = 5
data = [[1, 1], [5, 4], [6, 7], [7, -1], [2, 2], [0, 6], [0, 8], [56, 3], [0, 9], [0, -1]]
linkedList = []
for item in data:
    linkedList.append(Node(data=item[0], nextNode=item[1]))
# print(linkedList)

# c) i
def outputNodes(linkedList, pointer) -> None:
    while True:
        if (pointer == -1):
            break
        print(f"{linkedList[pointer].data}")
        pointer = linkedList[pointer].nextNode

# c) ii
outputNodes(linkedList=linkedList, pointer=startPointer)

# d) i)
def addNode(linkedList, currentPointer, emptyList) -> bool:
    
    data = input("?) Input data: ")
    try:
        data = int(data)
    except ValueError:
        print("addNode() -> `data` should be of type int")
        return False
    
    if (emptyList < 0) or (emptyList > 9):
        print("List is full")
        return False

    previous_pointer = 0
    while (currentPointer != -1):
        previous_pointer = currentPointer
        currentPointer = linkedList[currentPointer].nextNode
    linkedList[previous_pointer].nextNode = emptyList
    emptyList = linkedList[emptyList].nextNode
    return True
    
# d) ii)

rval = addNode(linkedList=linkedList, currentPointer=startPointer, emptyList=emptyList)
if rval is True:
    print("! Item added successfully")
else:
    print("! Item not added")
outputNodes(linkedList=linkedList, pointer=startPointer)
```

## Question 2

```python
# a)
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

# b) i
def linearSearch(searchFor: int):
    global arrayData
    for item in arrayData:
        if item == searchFor:
            return True
    return False

# b) ii
while True:
    inp = input("? Enter an integer: ").strip()
    try:
        if "." in inp: # float / decimal is entered
            raise ValueError
        inp = int(inp)
        break
    except ValueError:
        print("Please enter a valid integer")
    except Exception as e:
        print(f"Another error occured: {e}")
isFound = linearSearch(searchFor=inp)
if isFound is True:
    print(f"Found {inp} in `arrayData`")
else:
    print(f"{inp} NOT found in `arrayData`")

# c)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

done= bubbleSort(arr=arrayData)
print(done)
```

## Question 3

```python
# a)
class TreasureChest:
    def __init__(self, question: str, answer: int, points: int) -> None:
        self.__question = question
        self.__answer = answer
        self.__points = points

    def __repr__(self):
        return f"<TreasureChest question='{self.__question}' answer={self.__answer} points={self.__points}>"

    # c) i
    def getQuestion(self) -> str:
        return self.__question

    # c) ii
    def checkAnswer(self, answer: int) -> bool:
        if answer == self.__answer:
            return True
        else:
            return False

    # c) iii
    def getPoints(self, attempts) -> int:
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points) // 2
        elif attempts in [3, 4]:
            return int(self.__points) // 4
        else:
            return 0
    
# b)
arrTreasure = []
def readData():
    try:
        with open("TreasureChestData.txt", "r", encoding="utf-8") as file:
            dataFetched = (file.readline()).strip()
            while(dataFetched != "" ):
                question = dataFetched
                answer = int(file.readline().strip())
                points = int(file.readline().strip())
                arrTreasure.append(
                        TreasureChest(
                                question=question,
                                answer=answer,
                                points=points
                            )
                    )
                dataFetched = file.readline().strip() 
    except (IOError, FileNotFoundError):
        print("File not found")
    except Exception as e:
        print(f"Another error occured: {e}")


# c) iv
def inputInt(query: str) -> int:
    return int(input(query))

readData()
qnum = inputInt(query="? Pick treasure to open [1-5]: ")
if (qnum > 0) and (qnum < 6):
    result = False
    attempts = 0
    while (result == False):
        answer = inputInt(query=f"? Solve: {arrTreasure[qnum-1].getQuestion()} = ")
        result = arrTreasure[qnum-1].checkAnswer(answer=answer)
        attempts += 1
    print(f"! You have {arrTreasure[qnum-1].getPoints(attempts=attempts)} points.")

```
