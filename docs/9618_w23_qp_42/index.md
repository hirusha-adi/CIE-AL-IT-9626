---
title: "9618_w23_qp_42 (2022 Nov 42)"
sidebar_label: "9618_w23_qp_42"
---

<details>
<summary>Resources:</summary>

- [Question Paper](./9618_w23_qp_42.pdf)
- [Exam Resources](./9618_w23_sf_42.zip)
- [My Answers `(evidence.doc)`](./11_9618_42_SourceFiles/evidence.doc)

</details>

## Question 1

```python
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
```

## Question 2

```python
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

```

## Question 3

```python
import datetime


# a) i)
class Character:
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
        # self.__CharacterName string
        # self.__DateOfBirth date
        # self.__Intelligence real
        # self.__Speed integer
        self.__CharacterName = CharacterName
        self.__DateOfBirth = DateOfBirth
        self.__Intelligence = Intelligence
        self.__Speed = Speed

    # a) ii)
    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    # a) iii)
    def SetIntelligence(self, value):
        self.__Intelligence = value

    # a) iv)
    def Learn(self):
        self.__Intelligence *= 1.1

    # a) v)
    def ReturnAge(self):
        current_year = datetime.datetime.now().year
        return current_year - self.__DateOfBirth.year


# b) i)
FirstCharacter = Character(
    CharacterName="Royal",
    DateOfBirth=datetime.datetime(
        2019,
        1,
        1,
    ),
    Intelligence=70,
    Speed=30,
)

# b) ii)
FirstCharacter.Learn()
print(
    f"{FirstCharacter.GetName()} is {FirstCharacter.ReturnAge()} years old with an intelligence of {FirstCharacter.GetIntelligence()}"
)

# b) iii) screenshot


# c)
class MagicCharacter(Character):
    def __init__(self, Element, CharacterName, DateOfBirth, Intelligence, Speed):
        # self.__Element string

        super().__init__(
            CharacterName=CharacterName,
            DateOfBirth=DateOfBirth,
            Intelligence=Intelligence,
            Speed=Speed,
        )
        self.__Element = Element

    #
    def Learn(self):
        if (self.__Element == "fire") or (self.__Element == "water"):
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif self.__Element == "eart":
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)


# d) i)
FirstMagic = MagicCharacter(
    Element="fire",
    CharacterName="Light",
    DateOfBirth=datetime.datetime(2018, 3, 3),
    Intelligence=75,
    Speed=22,
)
FirstMagic.Learn()
print(
    f"{FirstMagic.GetName()} is {FirstMagic.ReturnAge()} years old with an intelligence of {FirstMagic.GetIntelligence()}"
)

```