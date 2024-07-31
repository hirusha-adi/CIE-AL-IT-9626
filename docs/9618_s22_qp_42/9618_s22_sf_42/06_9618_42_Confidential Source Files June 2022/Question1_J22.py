StackData = []
StackPointer = 0
MAX_SIZE = 10


def OutputStack() -> None:
    global StackData, StackPointer
    print(StackPointer)
    for data in StackData:
        print(data)


def Push(value: int) -> bool:
    global StackData, StackPointer
    # print("StackPointer", StackPointer, StackPointer >= MAX_SIZE)
    if StackPointer >= MAX_SIZE:
        # ("Stack is full!")
        return False
    else:
        # print("StackPointer else", StackPointer)
        StackPointer += 1
        StackData.append(value)
        return True


for i in range(11):
    while True:
        inp = input(f"Enter integer {i + 1}: ").strip()
        try:
            if "." in inp:
                raise ValueError
            inp = int(inp)
            break
        except ValueError:
            print("Please enter a valid integer")

    res = Push(value=inp)
    if not res:
        print("Stack is full!")
        break
    else:
        print(f"Stored {inp}")

OutputStack()


def Pop() -> int:
    global StackData, StackPointer
    if StackPointer == 0:
        print("Stack is empty!")
        return -1
    else:
        StackPointer -= 1
        return StackData.pop()


Pop()
Pop()
OutputStack()
