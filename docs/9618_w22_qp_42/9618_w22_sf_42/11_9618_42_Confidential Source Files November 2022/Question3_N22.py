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












