
# a)
Jobs = [] # global 2 dimentional array of type integer, 100 by 2 elements
NumberOfJobs = 0 # global integer

# b)
def Initialise():
    global Jobs
    global NumberOfJobs
    for i in range(0, 100):
        Jobs.append([-1, -1])
    NumberOfJobs = 0

# c)
def AddJob(JobNumber, Priority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs == 100:
        print("Not added") # our array is full
    else:
        Jobs[NumberOfJobs] = [JobNumber, Priority]
        print("Added")
        NumberOfJobs += 1

# d)
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

# e)
# PLEASE TAKE A LOOK AT THIS AGAIN
# since i have no idea about this, in the exam,
# use something like .sort() and continue to get marks for the others
# and also the final mark for the screen shot
def InsertionSort():
     global Jobs
     global NumberOfJobs
     for I in range(1, NumberOfJobs):
         Current1 = Jobs[I][0]
         Current2 = Jobs[I][1]
         while I > 0 and Jobs[I-1][1] > Current2:
             Jobs[I][0] = Jobs[I-1][0]
             Jobs[I][1] = Jobs[I-1][1]
             I = I - 1
         Jobs[I][0] = Current1
         Jobs[I][1] = Current2
# marks are given as follows:
# Procedure header (and end where appropriate)
# • Outer loop through all 5 elements / number of jobs …
# • … inner loop through array elements …
# • …and comparing priority (second index) …
# • …moving the elements up and inserting correctly


# f)
def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(0, NumberOfJobs):
        element = Jobs[i]
        print(f"{element[0]} priority {element[1]}")

# g) i)
InsertionSort()
PrintArray()

















