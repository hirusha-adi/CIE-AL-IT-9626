ArrayNodes = [[0 for i in range(3)] for j in range(20)]
RootPointer = -1
FreeNode = 0

def addNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the data: "))
    if FreeNode <= 19: # if not full
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        
        if RootPointer == -1: # if completely empty
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            
            while Placed == False: # until placed
                if NodeData < ArrayNodes[CurrentNode][1]: # if less than value
                    if ArrayNodes[CurrentNode][0] == -1: # if -1, place there
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else: # go to next node
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:   # is greater than value
                    if ArrayNodes[CurrentNode][2] == -1: # if -1, place there
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else: # go to next node
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode += 1 # go to next node

    else: # if full
        print("Tree is full!")
    
    return ArrayNodes, RootPointer, FreeNode

def printAll(ArrayNodes):
    print("LP | D | RP")
    for i in range(0, 20):
        if not((ArrayNodes[i][0] == 0) and (ArrayNodes[i][1] == 0) and (ArrayNodes[i][2] == 0)):
            print(f"{ArrayNodes[i][0]}  {ArrayNodes[i][1]}  {ArrayNodes[i][2]}")

print("---\nEnter Values\n---")
for X in range(0,10):
    ArrayNodes, RootPointer, FreeNode = addNode(ArrayNodes,RootPointer,FreeNode)
print("---\nOutput of `printAll`\n---")
printAll(ArrayNodes)


"""
> python .\Question3.py 
---
Enter Values
---
Enter the data: 10
Enter the data: 5
Enter the data: 15
Enter the data: 8
Enter the data: 12
Enter the data: 6
Enter the data: 20
Enter the data: 11
Enter the data: 9
Enter the data: 4
---
Output of `printAll`
---
LP | D | RP
1  10  2
9  5  3
4  15  6
5  8  8
7  12  -1
-1  6  -1
-1  20  -1
-1  11  -1
-1  9  -1
-1  4  -1
"""


def InOrder(ArrayNodes, RootNodes):
    if ArrayNodes[RootNodes][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNodes][0])
    print(ArrayNodes[RootNodes][1])
    if ArrayNodes[RootNodes][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNodes][2])

print("---\nOutput of `InOrder`\n---")
InOrder(ArrayNodes=ArrayNodes, RootNodes=RootPointer)

"""
> python .\Question3.py 
---
Enter Values
---
Enter the data: 10
Enter the data: 5
Enter the data: 15
Enter the data: 8
Enter the data: 12
Enter the data: 6
Enter the data: 20
Enter the data: 11
Enter the data: 9
Enter the data: 4
---
Output of `printAll`
---
LP | D | RP
1  10  2
9  5  3
4  15  6
5  8  8
7  12  -1
-1  6  -1
-1  20  -1
-1  11  -1
-1  9  -1
-1  4  -1
---
Output of `InOrder`
---
4
5
6
8
9
10
11
12
15
20
"""