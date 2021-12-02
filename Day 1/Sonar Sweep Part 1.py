
filename = input("Name of input file: ")
inputfile = open(filename,"r")

previousValue = int(inputfile.readline())
currentLine = inputfile.readline()
counter = 0

while currentLine != "":

    if int(currentLine) > previousValue:
        counter = counter + 1

    previousValue = int(currentLine)
    currentLine = inputfile.readline()

print("Answer: " + str(counter))    


