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
        
        
