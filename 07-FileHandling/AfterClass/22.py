import csv

with open('C:/Study/pp1/07-FileHandling/After class/students.txt', 'r') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for line in csv_reader:
        counter = 1
        if lineCount > 0:
            for row in line:
                if int (line[2])<30:
                    if counter == 1:
                        print(row, end = ' ')
                    if counter==2:
                        print(row, end = ' ')
                    if counter==5:
                        print(row)
                    counter = counter +1
        lineCount = lineCount + 1
