---
title: "9618_s23_qp_42 (2023 May 42)"
sidebar_label: "9618_s23_qp_42"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_s23_qp_42.pdf)
- [Exam Resources](./9618_s23_sf_42.zip)
- [My Answers `(evidence.doc)`](./06_9618_42_2023_source_files/evidence.doc)

</details>

## Question 1

```python
# Started at 1:00

# 1 (a)
Animals = ['']*10

# (b)
Animals[0] = "horse"
Animals[1] = "lion"
Animals[2] = "rabbit"
Animals[3] = "mouse"
Animals[4] = "bird"
Animals[5] = "deer"
Animals[6] = "whale"
Animals[7] = "elephant"
Animals[8] = "kangaroo"
Animals[9] = "tiger"

# (c)
def SortDescending():
    """bubble sort in descending order for Animals list"""
    global Animals
    n = len(Animals)
    for i in range(n):
        for j in range(0, n-i-1):
            if Animals[j][0] > Animals[j+1][0]:
                Animals[j], Animals[j+1] = Animals[j+1], Animals[j]

# (d)
def main():
    global Animals
    SortDescending()
    for animal in Animals:
        print(animal, end="\n")

if __name__ == "__main__":
    main()
    
# Completed at 1:09
    
```

## Question 2

```python
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
```

## Question 3

```python
# Started at 1:45

# (a)
class Employee:
    # self.__HourlyPay is a float
    # self.__EmployeeNumber is a string
    # self.__JobTitle is a string
    # self.__PayYear2022 is an array of length 52 consisting of floats
    
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay: float = HourlyPay
        self.__EmployeeNumber: str = EmployeeNumber
        self.__JobTitle: str = JobTitle
        self.__PayYear2022: str[float] = [0.00]*52 # 52 elements from index 0 to 51

    # (a) ii)
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    # (a) iii)
    def SetPay(self, WeekNumber, NoOfHours):
        if (WeekNumber < 0) or (WeekNumber > 52):
            raise ValueError("Invalid `WeekNumber`. Week Number is out of range. It should be between 0-52")
        # PLEASE remember to sub 1 from the index. human to index conversion thing
        self.__PayYear2022[WeekNumber-1] = self.__HourlyPay * NoOfHours

    # (a) iv)
    def GetTotalPay(self):
        total = 0
        for week in self.__PayYear2022:
            total += week
        return total

# (b)
class Manager(Employee):
    # self.__BonusValue is a float
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue = BonusValue
    
    def SetPay(self, WeekNumber, NoOfHours):
        NoOfHours = NoOfHours * (1 + (self.__BonusValue/100)) # from IGCSE Maths
        return super().SetPay(WeekNumber, NoOfHours)

# (c)

# EmployeeArray is array/list of Employee or Manager
EmployeeArray: list[Employee | Manager] = []*8 # from index 0 to 7
try:
    with open("Employees.txt", "r", encoding="utf-8") as _file:
        for i in range(0,8): # EmployeeArray
            hp = float(_file.readline())
            en = _file.readline().strip()           # THIS DOESNT WORK WHEN float(). I DONT KNOW WHY
            tmp = _file.readline()
            try:
                bs = float(tmp)
                tl = _file.readline()
                EmployeeArray.append(Manager(HourlyPay=hp,EmployeeNumber=en,JobTitle=tl,BonusValue=bs))
            except ValueError:
                EmployeeArray.append(Employee(HourlyPay=hp, EmployeeNumber=en, JobTitle=tmp))
except (FileNotFoundError, IOError):
    print("File: Employee.txt not found!")

def EnterHours():
    try:
        with open("HoursWeek1.txt", "r", encoding="utf-8") as f:
            for _ in range(0,8): # EmployeeArray
                en = f.readline()
                hrs = f.readline()
                for element  in EmployeeArray:
                    if element.GetEmployeeNumber() == en:
                        element.SetPay(1, float(hrs)) # week 1, no. of hours per week 1
    except (FileNotFoundError, IOError):
        print("File: Employee.txt not found!")

EnterHours()
for element in EmployeeArray:
    print(f"{element.GetEmployeeNumber()} - {element.GetTotalPay()}")

# Completed at 2:26
```
