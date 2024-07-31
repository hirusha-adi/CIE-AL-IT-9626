# 2) a) i)
def IterativeCalculate(number):
    to_find = number
    total = 0
    while True:
        if number == 0:
            break
        if to_find % number == 0:
            total += number
        number -= 1
    return total


# a) ii)
print(IterativeCalculate(number=10))


# b) i)
def RecursiveValue(number, to_find):
    if number == 0:
        return 0
    else:
        if to_find % number == 0:
            return number + RecursiveValue(number=number - 1, to_find=to_find)
        else:
            return RecursiveValue(number=number - 1, to_find=to_find)


# b) ii)
print(RecursiveValue(50, 50))
