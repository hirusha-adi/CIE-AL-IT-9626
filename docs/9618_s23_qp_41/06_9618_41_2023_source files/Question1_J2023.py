
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

