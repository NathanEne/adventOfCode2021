
filename = input("Name of input file: ")
inputfile = open(filename,"r")

valueOne = int(inputfile.readline())
valueTwo = int(inputfile.readline())
valueThree = inputfile.readline()
currentSum = valueOne +  valueTwo + int(valueThree)
counter = 0

#simulating a do-while loop in python
while True:

    valueOne = valueTwo
    valueTwo = int(valueThree)
    valueThree = inputfile.readline()

    if valueThree == "":
        break

    previousSum = currentSum
    currentSum = valueOne +  valueTwo + int(valueThree) 

    if currentSum > previousSum:
        counter = counter + 1
    

print("Answer: " + str(counter))    


