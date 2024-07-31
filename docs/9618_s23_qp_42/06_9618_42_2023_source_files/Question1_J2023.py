# Started at 1:00

# 1 (a)
Animals = ['']*10

# (b)
Animals[0] = "horse"
Animals[1] = "lion"
Animals[2] = "rabbit"
Animals[3] = "mouse"
Animals[4] = "bird"
Animals[5] = "deer"
Animals[6] = "whale"
Animals[7] = "elephant"
Animals[8] = "kangaroo"
Animals[9] = "tiger"

# (c)
def SortDescending():
    """bubble sort in descending order for Animals list"""
    global Animals
    n = len(Animals)
    for i in range(n):
        for j in range(0, n-i-1):
            if Animals[j][0] > Animals[j+1][0]:
                Animals[j], Animals[j+1] = Animals[j+1], Animals[j]

# (d)
def main():
    global Animals
    SortDescending()
    for animal in Animals:
        print(animal, end="\n")

if __name__ == "__main__":
    main()
    
# Completed at 1:09
    