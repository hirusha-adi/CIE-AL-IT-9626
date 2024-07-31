# a)
def Unknown(x: int, y: int) -> int:
    if x < y:
        print(x+y)
        return Unknown(x+1, y)*2
    elif x == y:
        return 1
    else:
        print(x+y)
        return int(Unknown(x-1, y)/2)

# b) i)
# Method 1: works dynamically
"""
# values_to_run = [[10, 15], [10, 10], [15, 10]]  
# for value in values_to_run:
#     print(f"+ Running `unknown()` with x={value[0]}, y={value[1]}")
#     Unknown(x=value[0], y=value[1])
# ---
# this outputs:
# ---
# + Running `unknown()` with x=10, y=15
# 25
# 26
# 27
# 28
# 29
# + Running `unknown()` with x=10, y=10
# + Running `unknown()` with x=15, y=10
# 25
# 24
# 23
# 22
# 21
"""

# b) i)
# Method 2: (from M/S)
print("Function: `Unknown(...)`\n-----------")
print("10 and 15")
print(Unknown(10, 15))
print("10 and 10")
print(Unknown(10, 10))
print("15 and 10")
print(Unknown(15, 10))     

# b) ii)
"""
> python .\Question1.py
Function: `Unknown(...)`
-----------
10 and 15
25
26
27
28
29
32
10 and 10
1
15 and 10
25
24
23
22
21
0
"""

# c)
# OOF - HELP - what exactly is the function of the original func
def IterativeUnknown(x, y):
    total = 1
    while x != y:
        print(x+y)
        if x < y:
            x += 1
            total = total * 2
        else:
            x -= 1
            total = int(total/2)
    return total

# d) i)
print("Function: `IterativeUnknown(...)`\n-----------")
print("10 and 15")
print(IterativeUnknown(10, 15))
print("10 and 10")
print(IterativeUnknown(10, 10))
print("15 and 10")
print(IterativeUnknown(15, 10))  

# d) ii)
"""
> python .\Question1.py
Function: `Unknown(...)`
-----------
10 and 15
25
26
27
28
29
32
10 and 10
1
15 and 10
25
24
23
22
21
0
Function: `IterativeUnknown(...)`
-----------
10 and 15
25
26
27
28
29
32
10 and 10
1
15 and 10
25
24
23
22
21
0
"""

 