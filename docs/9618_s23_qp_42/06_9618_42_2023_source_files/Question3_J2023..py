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
