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



