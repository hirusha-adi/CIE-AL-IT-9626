# a)
class Player:
    def __init__(self, name, score: int):
        self.__name = name
        self.__score = score

    def __repr__(self):
        return f"<Player name='{self.__name}' score={self.__score}>"

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def set_score(self, value):
        self.__score = value

PlayerData = []

# b)
def ReadHighScores():
    try:
        with open("HighScore.txt", "r", encoding="utf-8") as file:
            for i in range(10):
                name = file.readline().strip()[:3]
                try:
                    score = int(file.readline().strip())
                except ValueError:
                    print(f"Not an integer after {name}")
                PlayerData.append(Player(name=name, score=score))
    except (IOError, FileNotFoundError):
        print("File not found!")
    except Exception as e:
        print(f"Another errror occured: {e}")

# c) 
def OutputHighScores():
    for element in PlayerData:
        print(f"{element.name} {element.score}")
    
# d) i)
ReadHighScores()
OutputHighScores()

# d) ii)
# screenshot


# e) i)
while True:
    inp_name = input("?) Enter the player name: ").strip().upper()
    if len(inp_name) == 3:
        break

while True:
    inp_score = input("? Enter the player score: ").strip()
    try:
        if "." in inp_score:
            raise ValueError
        inp_score = int(inp_score)
        if (inp_score < 1) or (inp_score > 10000):
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid integer belonging to the given range!")
    except Exception as e:
        print(f"An other error occured: {e}")

# e) ii)
def Foo(name, score):
    last_item = PlayerData[-1]
    if inp_score > last_item.score:
        del PlayerData[-1]
        PlayerData.append(Player(name=name, score=score))
    else:
        print("Player doesn't belong to Top 10")

    n = len(PlayerData)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if PlayerData[j].score < PlayerData[j+1].score:
                PlayerData[j], PlayerData[j+1] = PlayerData[j+1], PlayerData[j]

# e) ii)
Foo(name=inp_name, score=inp_score)
OutputHighScores()

# f)
def WriteTopTen():
    with open("NewHighScore.txt", "w+", encoding='utf-8') as file:
        file.write(f"{PlayerData[0].name}\n{PlayerData[0].score}") # to fix the new line issue
        for el in PlayerData[1:]:
            file.write(f"\n{el.name}\n{el.score}")

WriteTopTen()
