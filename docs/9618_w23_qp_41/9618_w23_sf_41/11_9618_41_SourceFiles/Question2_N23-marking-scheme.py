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
