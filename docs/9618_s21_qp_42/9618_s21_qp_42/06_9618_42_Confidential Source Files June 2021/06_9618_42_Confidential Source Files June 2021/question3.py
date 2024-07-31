# a)
class TreasureChest:
    def __init__(self, question: str, answer: int, points: int) -> None:
        self.__question = question
        self.__answer = answer
        self.__points = points

    def __repr__(self):
        return f"<TreasureChest question='{self.__question}' answer={self.__answer} points={self.__points}>"

    # c) i
    def getQuestion(self) -> str:
        return self.__question

    # c) ii
    def checkAnswer(self, answer: int) -> bool:
        if answer == self.__answer:
            return True
        else:
            return False

    # c) iii
    def getPoints(self, attempts) -> int:
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points) // 2
        elif attempts in [3, 4]:
            return int(self.__points) // 4
        else:
            return 0
    
# b)
arrTreasure = []
def readData():
    try:
        with open("TreasureChestData.txt", "r", encoding="utf-8") as file:
            dataFetched = (file.readline()).strip()
            while(dataFetched != "" ):
                question = dataFetched
                answer = int(file.readline().strip())
                points = int(file.readline().strip())
                arrTreasure.append(
                        TreasureChest(
                                question=question,
                                answer=answer,
                                points=points
                            )
                    )
                dataFetched = file.readline().strip() 
    except (IOError, FileNotFoundError):
        print("File not found")
    except Exception as e:
        print(f"Another error occured: {e}")


# c) iv
def inputInt(query: str) -> int:
    return int(input(query))

readData()
qnum = inputInt(query="? Pick treasure to open [1-5]: ")
if (qnum > 0) and (qnum < 6):
    result = False
    attempts = 0
    while (result == False):
        answer = inputInt(query=f"? Solve: {arrTreasure[qnum-1].getQuestion()} = ")
        result = arrTreasure[qnum-1].checkAnswer(answer=answer)
        attempts += 1
    print(f"! You have {arrTreasure[qnum-1].getPoints(attempts=attempts)} points.")

# c) v

























        




