class Picture:
    def __init__(self, description: str, width: int, height: int, frame_color: str) -> None:
        self.__description = description
        self.__width = width
        self.__height = height
        self.__frame_color = frame_color
    
    def __repr__(self) -> str:
        return f"<Picture description='{self.__description}' width={self.__width} height={self.__height} frame_color={self.__frame_color}>"
    
    def getDescription(self) -> str:
        return self.__description

    def getWidth(self) -> int:
        return self.__width
    
    def getHeight(self) -> int:
        return self.__height
    
    def getColor(self) -> str:
        return self.__frame_color
    
    def setDescription(self, description: str) -> None:
        self.__description = description

pictures: list[Picture] = [] # basically a list of Picture

def readData():
    try:
        with open("Pictures.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                pictures.append(Picture(
                    description=lines[i].strip(),
                    width=int(lines[i+1].strip()),
                    height=int(lines[i+2].strip()),
                    frame_color=lines[i+3].strip(),
                ))        
        return len(pictures)
    except (FileNotFoundError, IOError):
        print("File not found!")        


print("---\n* Loading Pictures...")
readData()
print("+ Pictures loaded!")

print("---\nEnter Requirements:\n---")
color = input("? Frame Color: ").lower()
max_width = int(input("? Maximum Width: "))
max_height = int(input("? Maximum Height: "))

count = 0
for picture in pictures:
    cur_color = picture.getColor().lower()
    cur_width = picture.getWidth()
    cur_height = picture.getHeight()
    if (cur_color == color) and (cur_width<=max_width) and (cur_height<=max_height):
        count += 1
        print(f"""----
Picture {count}: {picture.getDescription()}
Width: {cur_width}
Height: {cur_height}
Color: {cur_color}""")
print("---")

if count == 0:
    print("- No results found!")

"""
> python .\Question2.py 
---
* Loading Pictures...
+ Pictures loaded!
---
Enter Requirements:
? Frame Color: BLACK
? Maximum Width: 100
? Maximum Height: 100
----
Picture 1: Flowers
Width: 45
Height: 50
Color: black
----
Picture 2: People
Width: 20
Height: 20
Color: black
----
Picture 3: Landscape
Width: 30
Height: 45
Color: black
----
Picture 4: Landscape
Width: 25
Height: 37
Color: black
----
Picture 5: People
Width: 50
Height: 40
Color: black
---

> python .\Question2.py 
---
* Loading Pictures...
+ Pictures loaded!
---
Enter Requirements:
---
? Frame Color: silver
? Maximum Width: 25
? Maximum Height: 25
---
- No results found!
"""

