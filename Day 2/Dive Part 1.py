filename = input("Name of input file: ")
inputfile = open(filename,"r")
depth = 0
horiz = 0

currentLine = inputfile.readline()

while currentLine != "":

    split = currentLine.split()

    if split[0] == "forward":
        horiz += int(split[1])

    elif split[0] == "up":
        depth -= int(split[1])

    elif split[0] == "down":
        depth += int(split[1])

    currentLine = inputfile.readline()

print("Answer: " + str(horiz*depth))
