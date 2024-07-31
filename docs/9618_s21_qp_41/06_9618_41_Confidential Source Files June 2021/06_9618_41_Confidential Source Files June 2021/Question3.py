# REMEMBER THE READING FROM FILE THING

class TreasureChest:
    def __init__(self, question: str, answer: int, points: int) -> None:
        self.__question = question
        self.__answer = answer
        self.__points = points

    def __repr__(self):
        return f"<TreasureChest question='{self.__question}' answer={self.__answer} points={self.__points}>"        
    
    def getQuestion(self) -> str:
        return self.__question
    
    def checkAnswer(self, answer: int) -> bool:
        if answer == self.__answer:
            return True
        return False

    def getPoints(self, attempts: int):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return (self.__points//2)
        elif attempts in (3, 4):
            return (self.__points//4)
        else:
            return 0
        
arrayTreasure: list[TreasureChest] = []
def readData():
    arrayTreasure
    try:
        with open("TreasureChestData.txt", "r", encoding='utf-8') as _file:
            lines = _file.readlines()
            for i in range(0, len(lines), 3): # reading 3 lines at a time
                arrayTreasure.append(TreasureChest(
                    question=lines[i].strip(),
                    answer=int(lines[i+1].strip()),
                    points=int(lines[i+2].strip())
                ))
    except (FileNotFoundError, IOError):
        print("File not found in current working directory!")
    # print(arrayTreasure)


readData()
while True:
    question_index = input("[?] Enter a question number between 1-5: ")
    try:
        if "." in question_index:
            raise ValueError 
        question_index = int(question_index)
        if not(question_index in [1, 2, 3, 4, 5]):
            raise ValueError 
        question_index -= 1 # fix index from normal 1-5 to 0-4 as in array
        break
    except ValueError:
        print("Please enter a valid input.") 
obj = arrayTreasure[question_index]
count = 1
while True:
    print("[?] Question: ", obj.getQuestion())
    answer = int(input("[?] >> "))
    is_correct = obj.checkAnswer(answer=answer)
    if is_correct:
        points = obj.getPoints(attempts=count)
        print(f"[+] Points Scored: {points}")
        break
    print("[-] Incorrect Answer. Please retry!\n")
    count += 1
    
    
"""
> python .\Question3.py
[?] Enter a question number between 1-5: 1
[?] Question:  2*2
[?] >> 4
[+] Points Scored: 10

> python .\Question3.py
[?] Enter a question number between 1-5: 5
[?] Question:  3000+4000
[?] >> 8980
[-] Incorrect Answer. Please retry!

[?] Question:  3000+4000
[?] >> 7000
[+] Points Scored: 9
"""