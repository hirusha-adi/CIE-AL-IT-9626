# Started at 1:09

# (a)
# ---
class SaleData:
    def __init__(self, id_="", quantity=-1):
        self.id_ = id_
        self.quantity = quantity
    
    def __repr__(self):
        return f"<SaleData id='{self.id_}' quantity={self.quantity}>"

# (b)
CircularQueue = [SaleData()]*5 # of 5 items to store the sale records
Head = 0
Tail = 0
NumberOfItems = 0

# (c)
def Enqueue(RecordToAdd):
    global CircularQueue, Head, Tail, NumberOfItems
    if(NumberOfItems == 5):
        return -1
    else:
        CircularQueue[Tail] = RecordToAdd
        if(Tail == 4):
            Tail = 0
        else:
            Tail +=1
            NumberOfItems +=1
        return 1

# (d)
def Dequeue():
    global CircularQueue, Head, Tail, NumberOfItems
    
    if NumberOfItems == 0:
        return SaleData()
    
    record = CircularQueue[Head]

    # PLEASE REMEMBER THIS
    Head = (Head + 1) % len(CircularQueue)  # Circular increment
    NumberOfItems -= 1
    
    return record

# (e)
def EnterRecord():
    id_ = input("Enter ID: ")
    quantity = input("Enter Quantity: ")
    r = Enqueue(SaleData(id_=id_, quantity=quantity))
    if r == -1:
        print("Full")
    else:
        print("Stored")

# (f)
def main():
    for _ in range(0, 6):
        EnterRecord()
    dequeued_record = Dequeue()
    if dequeued_record.id_ == "":
        print("No items")
    else:
        print(f"De-Queued element: {dequeued_record}")
    EnterRecord()
    for i in CircularQueue:
        print(i)
    
if __name__ == "__main__":
    main()

# Completed at 1:40
# my Enqueue() function was wrong. PLEASE LEARN MORE LATER.