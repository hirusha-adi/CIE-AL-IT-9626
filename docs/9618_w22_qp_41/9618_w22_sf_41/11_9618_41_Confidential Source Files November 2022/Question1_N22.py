
# a)
DataArray = [] # 100 integers

# b)
def ReadFile() -> None:
    global DataArray
    try:
        with open("IntegerData.txt", "r", encoding="utf-8") as _file:
            for line in _file.readlines():
                try:
                    DataArray.append(int(line.strip()))
                except ValueError:
                    print(f"{line.strip()} is not an integer in the text file. Skipping...")
    except (IOError, FileNotFoundError):
        print("File not found!")
    except Exception as e:
        print(f"Error: {e}")


# c)
def FindValues() -> int:
    global DataArray
    while True:
        value = input("[?] Enter a value to search for: ").strip().replace("_", "")
        try:
            if "." in value: # prevent the user from entering floats (decimal numbers)
                raise ValueError
            value = int(value)
            break
        except ValueError:
            print("Please enter a valid integer!")
        except Exception as e:
            print(f"Error: {e}")
    count = 0
    for el in DataArray:
        if value == el:
            count += 1
    
    return count
    
# d) i)
ReadFile()
count = FindValues()
print(f"The number was found {count} times")

# d) ii)
# screenshot

# e)
def BubbleSort():
    global DataArray
    n = len(DataArray)
    for i in range (n-1):
        for j in range(0, n-i-1):
            if DataArray[j] > DataArray[j+1]:
                DataArray[j], DataArray[j+1] = DataArray[j+1], DataArray[j]

BubbleSort()
print(DataArray)













