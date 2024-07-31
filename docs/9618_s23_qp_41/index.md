---
title: "9618_s23_qp_41 (2023 May 41)"
sidebar_label: "9618_s23_qp_41"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_s23_qp_41.pdf)
- [Exam Resources](./9618_s23_sf_41.zip)
- [My Answers `(evidence.doc)`](./06_9618_41_2023_source%20files/evidence.doc)

</details>

## Question 1

```python

# 1. A program reads data from a file and searches for specific data.
# ---


# (i) Write program code to declare the local array DataArray
# ---
DataArray = []


# (ii) Amend the main program to read the contents of Data.txt into DataArray
# ---
with open("Data.txt", "r", encoding='utf-8') as _file:
     for line in _file.readlines():
        line = line.strip()
        try:
            DataArray.append(int(line))
        except ValueError:
            pass # not an int
# print(DataArray)


# (b) (i) The procedure PrintArray() takes an integer array as a parameter 
# and outputs the contents of the array in the order they are stored.
# ---
def PrintArray(arr):
    for i in arr:
        print(i, end=" ")
    print()
# PrintArray(DataArray)

# (ii) Amend the main program to output the contents of DataArray using the procedure PrintArray()
# ---
PrintArray(DataArray)

# (c) The function LinearSearch():
# • takes an integer array and integer search value as parameters
# • counts and returns the number of times the search value is found in the array.
# Write program code for the function LinearSearch()
# ---
def LinearSearch(arr, val):
    count = 0
    for item in arr:
        if val == item:
            count += 1
    return count


# (d) (i) Amend the main program to:
# • prompt the user to input a whole number between 0 and 100 inclusive
# • read and validate the input from the user
# • call LinearSearch() with DataArray and the validated input value
# • output the result in the format:
# The number 7 is found 2 times.
# ---
while True:
    unum = input("Input a whole number [0-100]: ") 
    try:
        if "." in unum:
            raise ValueError # if a decimal number is enetered
                             # eg: will also block inputs like 7.0
        unum = int(unum)
        if (unum >= 0) and (unum <= 100):
            break # break out of loop if the user input is in range
        else:
            print(f"{unum} is not between 0-100. Please try again")
    except (ValueError,TypeError):
        print("Please input an integer")
count = LinearSearch(arr=DataArray, val=unum)
print(f"The number {unum} os found {count} times.")


# (ii) Test your program by inputting the number 12.
# Take a screenshot of the output.
# ---
# OUTPUT:
# 
# 10 4 5 13 25 31 4 66 12 5 0 11 15 20 21 12 33 49 12 12 7 7 4 22 0 
# Input a whole number [0-100]: 12
# The number 12 os found 4 times.

# 1+4+3+1+1+3+4+1 = 18 marks total

```

## Question 2

```python
# (a) (i)
# Write program code to declare the class Vehicle. All attributes must be private.
# You only need to declare the class and its constructor. Do not declare any other methods.
# Use your programming language’s appropriate constructor.
# If you are writing program code in Python, include attribute declarations using comments.
# ---
class Vehicle:
    def __init__(self, id, MaxSpeed, IncreaseAmount):
        self._id = id
        self._MaxSpeed = MaxSpeed
        self._IncreaseAmount = IncreaseAmount
        self._CurrentSpeed = 0
        self._HorizontalPosition = 0
    
    # (ii) Write program code for the get methods GetCurrentSpeed(),GetIncreaseAmount(), GetMaxSpeed() and GetHorizontalPosition()
    # ---
    @property
    def CurrentSpeed(self):
        return self._CurrentSpeed

    @property
    def IncreaseAmount(self):
        return self._IncreaseAmount
      
    @property
    def MaxSpeed(self):
        return self._MaxSpeed

    @property
    def HorizontalPosition(self):
        return self._HorizontalPosition
    
    # (iii) Write program code for the set methods SetCurrentSpeed() and SetHorizontalPosition()
    # ---
    @CurrentSpeed.setter
    def set_CurrentSpeed(self, value):
        self._CurrentSpeed = value
    
    @HorizontalPosition.setter
    def set_HorizontalPosition(self, value):
        self._HorizontalPosition = value
    
    
    # (iv) The method IncreaseSpeed():
    # • adds IncreaseAmount to the current speed
    # • adds the updated current speed to the horizontal position.
    # The current speed of a vehicle cannot exceed its maximum speed.
    # Write program code for the method IncreaseSpeed()
    # ---
    def IncreaseSpeed(self):
        if self._CurrentSpeed < self._MaxSpeed:
            self._CurrentSpeed += self._IncreaseAmount
            self._HorizontalPosition += self._CurrentSpeed
            

# (b) The child class Helicopter inherits from the parent class Vehicle. A helicopter also has a
# vertical position and changes the vertical position when it increases speed.    
# (i) Write program code to declare the class Helicopter. You only need to declare the
# class and its constructor. You do not need to declare the other methods.
# Use your programming language’s appropriate constructor.
# All attributes must be private.
# If you are writing in Python, include attribute declarations using comments.
# ---
class Helicopter(Vehicle):
    def __init__(self, id, MaxSpeed, IncreaseAmount, VerticalPosition, VerticalChange, MaxHeight):
        super().__init__(id, MaxSpeed, IncreaseAmount)
        self._VerticalPosition = VerticalPosition
        self._VerticalChange = VerticalChange
        self._MaxHeight = MaxHeight
    
    # GetVerticalPosition() getter
    @property
    def VerticalPosition(self):
        return self._VerticalPosition

    # (ii) The Helicopter method IncreaseSpeed() overrides the method from the parent
    # class and:
    # • adds the amount of vertical change to the vertical position
    # • adds IncreaseAmount to the current speed
    # • adds the updated current speed to the horizontal position.
    # The vertical position of a helicopter cannot exceed its maximum height.
    # The current speed of a helicopter cannot exceed its maximum speed.
    # Write program code for the method IncreaseSpeed()
    # ---
    def IncreaseSpeed(self):
        if self._VerticalPosition < self._MaxHeight:
            self._VerticalPosition += self._VerticalChange
            if self._CurrentSpeed < self._MaxSpeed:
                self._CurrentSpeed += self._IncreaseAmount
                self._HorizontalPosition += self._CurrentSpeed
    
# (c) A procedure needs to output the horizontal position and speed of a vehicle. If the vehicle is a
# helicopter, it also outputs the vertical position.
# All outputs must include appropriate messages.
# Write program code for this procedure.
# ---
def getSpeedAndPosition(obj):
    if isinstance(obj, Helicopter):
        print(f"(Helicopter)\n\tSpeed: {obj.CurrentSpeed}\n\tHorizontal Position: {obj.HorizontalPosition}\n\tVertical Position: {obj.VerticalPosition}")
    elif isinstance(obj, Vehicle):
        print(f"(Vehicle)\n\tSpeed: {obj.CurrentSpeed}\n\tHorizontal Position: {obj.HorizontalPosition}")
# # another approach is to use the __repr__ or __str__ dunder methods in the classes. 
# This is much for professional and its like production ready code. 
# This is the best way to do it. But then, what was even the purpose of writing 
# those getters and setters if we are not going to use them. 
# So, I settled with this


# (d) The main program needs to:
# • instantiate a car as a new vehicle with the ID "Tiger", a maximum speed of 100 and an
#   increase amount of 20
# • instantiate a new helicopter with the ID "Lion", a maximum speed of 350, an increase
#   amount of 40, a vertical change of 3 and a maximum height of 100
# • call IncreaseSpeed() twice for the car and then call the output procedure from
#   part 2(c) for the car
# • call IncreaseSpeed() twice for the helicopter and then call the output procedure from
#   part 2(c) for the helicopter.
# Write program code for the main program
# ---
def main():
    car = Vehicle(id="Tiger", MaxSpeed=100, IncreaseAmount=20)
    heli = Helicopter(id="Lion", MaxSpeed=350, IncreaseAmount=40, VerticalChange=3, MaxHeight=100, VerticalPosition=0)
    car.IncreaseSpeed()
    car.IncreaseSpeed()
    heli.IncreaseSpeed()
    heli.IncreaseSpeed()
    getSpeedAndPosition(car)
    getSpeedAndPosition(heli)

if __name__ == "__main__":
    main()

# 5+3+3+3+5+4+3+5+1 = 32 total marks
```

## Question 3

```python
# 3 A program implements two stacks using 1D arrays. One stack stores the names of colours. One
# stack stores the names of animals.
# (a) The program contains the following global arrays and variables:
# • 1D array Animal to store the names of up to 20 animals.
# • 1D array Colour to store the names of up to 10 colours.
# • AnimalTopPointer to point to the next free space in the array Animal, initialised to 0.
# • ColourTopPointer to point to the next free space in the array Colour, initialised to 0.
# Write program code to declare the global arrays and variables.
# ---
# PLEASE MAKE SURE TO INITIALIZE THIS
Animal = ['']*20 # to store the names of up to 20 animals
Colour = ['']*10 # to store the names of up to 10 colours
AnimalTopPointer = 0 # to point to the next free space in the array Animal
ColourTopPointer = 0 # to point to the next free space in the array Colour


# (b) (i) Study the pseudocode function PushAnimal():
# FUNCTION PushAnimal(DataToPush : STRING) RETURNS BOOLEAN
# IF AnimalTopPointer = 20 THEN
# RETURN FALSE
# ELSE
# Animal[AnimalTopPointer]
#  DataToPush
# AnimalTopPointer
#  AnimalTopPointer + 1
# RETURN TRUE
# ENDIF
# ENDFUNCTION
# Write program code for the function PushAnimal()
# ---
def PushAnimal(DataToPush: str) -> bool:
    global Animal, AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True


# (ii) Study the pseudocode function PopAnimal():
# FUNCTION PopAnimal() RETURNS STRING
# DECLARE ReturnData : STRING
# IF AnimalTopPointer = 0 THEN
# RETURN ""
# ELSE
# ReturnData
#  Animal[AnimalTopPointer - 1]
# AnimalTopPointer
#  AnimalTopPointer - 1
# RETURN ReturnData
# ENDIF
# ENDFUNCTION
# Write program code to declare the function PopAnimal()
# ---
def PopAnimal() -> str:
    global Animal, AnimalTopPointer
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


# (iii) The procedure ReadData():
# • reads the animal names from the file AnimalData.txt
# • uses PushAnimal() to insert each name onto the stack
# • uses appropriate exception handling if the file does not exist.
# Write program code for the procedure ReadData()
# ---
def ReadData():
    try:
        # import os # not the best practice to import it here, but works.
        # if not os.path.isfile(os.getcwd(), "AnimalData.txt"):
            # raise FileNotFoundError
        with open("AnimalData.txt", "r", encoding="utf-8") as _file:
            for animal in _file.readlines():
                PushAnimal(animal.strip())
    except FileNotFoundError:
        print("AnimalData.txt Not Found")
    except Exception as e:
        print(f"An error occured: {e}")
    
    # (v) Amend the procedure ReadData() so that it also:
    # • reads the colours from the text file ColourData.txt
    # • uses PushColour() to insert each colour onto the stack
    # • uses appropriate exception handling if the file does not exist.
    # ---
    try:
        # import os # not the best practice to import it here, but works.
        # if not os.path.isfile(os.getcwd(), "ColourData.txt"):
            # raise FileNotFoundError
        with open("ColourData.txt", "r", encoding="utf-8") as _file:
            for colour in _file.readlines():
                PushColour(colour.strip())
    except FileNotFoundError:
        print("ColourData.txt Not Found")
    except Exception as e:
        print(f"An error occured: {e}")
    

# (iv) The function PushColour() performs the same actions as PushAnimal() but inserts
# an item into Colour.
# The function PopColour() performs the same actions as PopAnimal() but removes
# the next item from Colour.
# Write program code for the functions PushColour() and PopColour()
# ---
def PushColour(DataToPush: str) -> bool:
    global Colour, ColourTopPointer
    if ColourTopPointer == 10: # only 10 elements
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True

def PopColour() -> str:
    global Colour, ColourTopPointer
    ReturnData = ""
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData


# (c) The procedure OutputItem():
#   • pops the next item from both Animal and Colour
#   • outputs the colour and animal on one line, for example "black horse"
# If there is no data in Colour:
#   • the animal is pushed back onto Animal
#   • "No colour" is output.
# If there is no data in Animal:
#   • the colour is pushed back onto Colour
#   • "No animal" is output.
# Write program code for the procedure OutputItem()
# ---
def OutputItem():
    panimal = PopAnimal()
    pcolour = PopColour()
    if pcolour == "":       # should work because we used .strip() when pushing, it also removed the empty lines
        PushAnimal(panimal)
        print("No colour")
    elif panimal == "":
        PushColour(pcolour)
        print("No Animal")
    else:
        print(f"{pcolour} {panimal}")


# (d) The main program:
# • calls the procedure ReadData()
# • calls OutputItem() four times.
# (i) Write program code for the main program.
# ---
def main():
    ReadData()
    OutputItem() # 1st time
    OutputItem() # 2nd time
    OutputItem() # 3rd time
    OutputItem() # 4th time

if __name__ == "__main__":
    main()

# 3+3+3+5+2+2+5+1+1+1 = 26 total marks
```
