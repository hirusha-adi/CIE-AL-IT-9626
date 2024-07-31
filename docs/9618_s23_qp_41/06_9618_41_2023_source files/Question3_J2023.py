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