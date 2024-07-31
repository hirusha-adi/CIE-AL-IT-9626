---
title: "9618_s21_qp_41 (2021 May 41)"
sidebar_label: "9618_s21_qp_41"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_s21_qp_41.pdf)
- [Exam Resources](./9618_s21_sf_41.zip)
- [My Answers `(evidence.doc)`](./06_9618_41_Confidential%20Source%20Files%20June%202021/06_9618_41_Confidential%20Source%20Files%20June%202021/evidence.doc)

</details>

## Question 1

```python
# a)
class node:
    def __init__(self, data: int,nextNode: int) -> None:
        self.data = data
        self.nextNode = nextNode

# b)
startPointer = 0
emptyList = 5    
linkedList: list[node] = [
    node(1, 1), # index 0
    node(5, 4),
    node(6, 7),
    node(7, -1),
    node(2, 2),
    node(0, 6),
    node(0, 8),
    node(56, 3),
    node(0, 9),
    node(0, -1) # index 9
]

# c) i)
def outputNodes(linkedList, currentPointer):
    while currentPointer != -1:
        print(linkedList[currentPointer].data)
        # print(linkedList[currentPointer].data, f"is at index: {currentPointer}")
        currentPointer = linkedList[currentPointer].nextNode

# outputNodes(linkedList=linkedList, currentPointer=startPointer)

# c) ii)
"""
> python .\Question1.py
1
5
2
6
56
7
"""


# d) i)
def addNode(linkedList, currentPointer, emptyList):
    
    avialable_idx = []
    for i in range(0, 10):
        avialable_idx.append(i)
    if (emptyList < 0) or (emptyList > 9):
        return False
    else:
        uinp = input("Enter the data to add: ")
        previousLastIdx = None
        while currentPointer != -1:
            avialable_idx.remove(currentPointer)
            previousLastIdx = currentPointer
            # print(linkedList[currentPointer].data, f"is at index: {currentPointer}")
            currentPointer = linkedList[currentPointer].nextNode
        if len(avialable_idx) == 0:
            return False
        linkedList[avialable_idx[0]] = node(data=int(uinp), nextNode=-1)
        linkedList[previousLastIdx].nextNode = avialable_idx[0]
        return True
        
# d) ii)
# enter '5' as the input
outputNodes(linkedList=linkedList, currentPointer=startPointer)
print("="*5)
r = addNode(linkedList=linkedList, currentPointer=startPointer, emptyList=emptyList)
if r:
    print("Item added successfully!")
else:
    print("Cannot add item. LinkedList is already full.")
print("="*5)
outputNodes(linkedList=linkedList, currentPointer=startPointer)


# d) iii)
"""
> python .\Question1.py
1
5
2
6
56
7
=====
Enter the data to add: 5
Item added successfully!
=====
1
5
2
6
56
7
5
"""
```

## Question 2

```python
# a)
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

# b) i)
def linearSearch(search_for: int) -> bool:
    global arrayData
    for element in arrayData:
        if search_for == element:
            return True
    return False

# b) ii)
while True:
    try:
        value = input("[?] Input an integer: ")
        if "." in value:    # if decimal number
            raise ValueError
        value = int(value)
        break
    except ValueError:
        print("[!!] Please enter a valid integer!")
        
# print(value, type(value))
is_found = linearSearch(search_for=value)
if is_found:
    print(f"[+] Found {value} in array `arrayData`")
else:
    print(f"[-] Not found {value} in array `arrayData`")
    
# d) iii)

"""
> python .\Question2.py
[?] Input an integer: 99
[-] Not found 99 in array `arrayData`

> python .\Question2.py
[?] Input an integer: 5
[+] Found 5 in array `arrayData`
"""

# c)
def bubbleSort():
    global arrayData
    for i in range(len(arrayData)):
        for j in range(len(arrayData)-i-1):
            if arrayData[j] > arrayData[j+1]:
                arrayData[j], arrayData[j+1] = arrayData[j+1], arrayData[j]

print("[+] Original Array: ", arrayData)
bubbleSort()
print("[+] Sorted Array: ", arrayData)

```

## Question 3

```python
# REMEMBER THE READING FROM FILE THING

class TreasureChest:
    def __init__(self, question: str, answer: int, points: int) -> None:
        self.__question = question
        self.__answer = answer
        self.__points = points

    def __repr__(self):
        return f"<TreasureChest question='{self.__question}' answer={self.__answer} points={self.__points}>"        
    
    def getQuestion(self) -> str:
        return self.__question
    
    def checkAnswer(self, answer: int) -> bool:
        if answer == self.__answer:
            return True
        return False

    def getPoints(self, attempts: int):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return (self.__points//2)
        elif attempts in (3, 4):
            return (self.__points//4)
        else:
            return 0
        
arrayTreasure: list[TreasureChest] = []
def readData():
    arrayTreasure
    try:
        with open("TreasureChestData.txt", "r", encoding='utf-8') as _file:
            lines = _file.readlines()
            for i in range(0, len(lines), 3): # reading 3 lines at a time
                arrayTreasure.append(TreasureChest(
                    question=lines[i].strip(),
                    answer=int(lines[i+1].strip()),
                    points=int(lines[i+2].strip())
                ))
    except (FileNotFoundError, IOError):
        print("File not found in current working directory!")
    # print(arrayTreasure)


readData()
while True:
    question_index = input("[?] Enter a question number between 1-5: ")
    try:
        if "." in question_index:
            raise ValueError 
        question_index = int(question_index)
        if not(question_index in [1, 2, 3, 4, 5]):
            raise ValueError 
        question_index -= 1 # fix index from normal 1-5 to 0-4 as in array
        break
    except ValueError:
        print("Please enter a valid input.") 
obj = arrayTreasure[question_index]
count = 1
while True:
    print("[?] Question: ", obj.getQuestion())
    answer = int(input("[?] >> "))
    is_correct = obj.checkAnswer(answer=answer)
    if is_correct:
        points = obj.getPoints(attempts=count)
        print(f"[+] Points Scored: {points}")
        break
    print("[-] Incorrect Answer. Please retry!\n")
    count += 1
    
    
"""
> python .\Question3.py
[?] Enter a question number between 1-5: 1
[?] Question:  2*2
[?] >> 4
[+] Points Scored: 10

> python .\Question3.py
[?] Enter a question number between 1-5: 5
[?] Question:  3000+4000
[?] >> 8980
[-] Incorrect Answer. Please retry!

[?] Question:  3000+4000
[?] >> 7000
[+] Points Scored: 9
"""
```

