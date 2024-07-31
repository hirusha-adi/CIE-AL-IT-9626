# a)
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

# b) i
def linearSearch(searchFor: int):
    global arrayData
    for item in arrayData:
        if item == searchFor:
            return True
    return False

# b) ii
while True:
    inp = input("? Enter an integer: ").strip()
    try:
        if "." in inp: # float / decimal is entered
            raise ValueError
        inp = int(inp)
        break
    except ValueError:
        print("Please enter a valid integer")
    except Exception as e:
        print(f"Another error occured: {e}")
isFound = linearSearch(searchFor=inp)
if isFound is True:
    print(f"Found {inp} in `arrayData`")
else:
    print(f"{inp} NOT found in `arrayData`")

# c)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

done= bubbleSort(arr=arrayData)
print(done)
