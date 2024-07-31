# a) i)
def IterativeVowels(Value):
    # Value string
    # IterateVowels() returns integer
    Total = 0
    for x in range(0, len(Value)):
        FirstCharacter = Value[0].lower()
        if FirstCharacter in ["a", "e", "i", "o", "u"]:
            Total += 1
        Value = Value[1:len(Value)]
    return Total

# a) ii)
print(IterativeVowels("house"))

# b) i)
def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    else:
        fch = Value[0]
    if fch in ["a", "e", "i", "o", "u"]:
        return 1 + RecursiveVowels(Value[1:len(Value)])
    else:
        return RecursiveVowels(Value[1:len(Value)])
    
# b) ii
print(RecursiveVowels("imagine"))
