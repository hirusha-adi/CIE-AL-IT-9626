
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
