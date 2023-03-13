import os.path 
import sys
import random 

def exercise1(): 
    word = input("Enter the string to be removed: ")
    infile = open("Family.txt", "r")
    outfile = open("Family2.txt", "w")

    for line in infile: 
        line = line.replace(word, " ")
        outfile.write(line)

def exercise2(): 
    infile = open("Family.txt", "r")
    countLines = countChars = countWords = 0 
    for line in infile: 
        countLines += 1 
        countChars += len(line)
        values = line.split() 
        countWords += len(values)

    print(countChars, "characters")
    print(countWords, "words")
    print(countLines, "lines")

    infile.close()

def exercise3(): 
    print("Enter a filename: ", end = " ")
    fileName = input()

    infile = open(fileName, "r")

    sum = totalScores = 0 
    line = infile.readline()
    while line:
        values = line.split() 
        for items in values: 
            sum += int(items)
        
        totalScores += len(values)
        line = infile.readline() 

    averageScore = sum / totalScores 

    print("There are", totalScores, "scores")
    print("The total is", sum)
    print("The average is", averageScore)

def exercise4(): 

    print("Enter a filename: ", end = " ")
    fileName = input()
    if os.path.isfile(fileName): 
        print("The file already exists")
        sys.exit()

    outfile = open(fileName, "w")  


    for i in range(100): 
        outfile.write(str(random.randint(0,100)) + " ")

    outfile.close()

    infile = open(fileName, "r")
    s = infile.read()

    numbers = [eval(x) for x in s.split()]
    numbers.sort()
    print(numbers)

    infile.close()

def exercise5(): 

    print("Enter a filename: ", end = " ")
    fileName = input()

    infile = open("Family2.txt", "r")
    outfile = open(fileName, "w")

    print("Enter the old string to be repalced:", end = " ")
    oldString = input() 

    print("Enter the string to replace the old string: ", end =" ")
    newString = input() 

    for line in infile: 
        line = line.replace(oldString, newString)
        outfile.write(line)

    infile.close()
    outfile.close() 



