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