# a)
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

# b) i)
def linearSearch(search_for: int) -> bool:
    global arrayData
    for element in arrayData:
        if search_for == element:
            return True
    return False

# b) ii)
while True:
    try:
        value = input("[?] Input an integer: ")
        if "." in value:    # if decimal number
            raise ValueError
        value = int(value)
        break
    except ValueError:
        print("[!!] Please enter a valid integer!")
        
# print(value, type(value))
is_found = linearSearch(search_for=value)
if is_found:
    print(f"[+] Found {value} in array `arrayData`")
else:
    print(f"[-] Not found {value} in array `arrayData`")
    
# d) iii)

"""
> python .\Question2.py
[?] Input an integer: 99
[-] Not found 99 in array `arrayData`

> python .\Question2.py
[?] Input an integer: 5
[+] Found 5 in array `arrayData`
"""

# c)
def bubbleSort():
    global arrayData
    for i in range(len(arrayData)):
        for j in range(len(arrayData)-i-1):
            if arrayData[j] > arrayData[j+1]:
                arrayData[j], arrayData[j+1] = arrayData[j+1], arrayData[j]

print("[+] Original Array: ", arrayData)
bubbleSort()
print("[+] Sorted Array: ", arrayData)

