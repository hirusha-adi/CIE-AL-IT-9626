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
