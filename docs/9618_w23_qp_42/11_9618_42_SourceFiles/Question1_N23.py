# a) i)
# # ---
StackVowel = []  # string 100
StackConsonant = []  # string 100

# a) ii)
# ---
VowelTop = 0
ConsonantTop = 0


# b) i)
def PushData(letter: str):
    global VowelTop, StackVowel
    global ConsonantTop, StackConsonant
    if letter.strip().lower() in ["a", "e", "i", "o", "u"]:
        if VowelTop == 100:
            print("[!!] Vowel stack is full!")
        else:
            StackVowel.append(letter)
            VowelTop += 1
    else:
        if StackConsonant == 100:
            print("[!!] Consonant stack is full!")
        else:
            StackConsonant.append(letter)
            ConsonantTop += 1


# b) ii)
def ReadData():
    with open("StackData.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            PushData(letter=line)


# c) i)
def PopVowel():
    global VowelTop, StackVowel
    if VowelTop >= 0:
        VowelTop -= 1
        ret = StackVowel[VowelTop]
        del StackVowel[VowelTop]
        return ret
    else:
        return "No data"


def PopConsonant():
    global ConsonantTop, StackConsonant
    if ConsonantTop >= 0:
        ConsonantTop -= 1
        ret = StackConsonant[ConsonantTop]
        del StackConsonant[ConsonantTop]
        return ret
    else:
        return "No data"


# d) i)
ReadData()

txt = ""
for _ in range(0, 5):
    while True:
        inp = input("[?] Enter a vowel or a consonant: ").strip().lower()
        if inp == "vowel":
            func = PopVowel
        else:
            func = PopConsonant
        popped = func()
        if popped == "No data":
            print("[!!] No vowels in the vowel stack")
        else:
            txt += popped.strip()
            break

print(txt)
