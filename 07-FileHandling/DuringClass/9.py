file = open('C:/Study/pp1/07-FileHandling/During class/numbers.txt')
lst = []
for line in file:
    line = line.rstrip()
    lineInt = int(line)
    lst.append(lineInt)
print(sum(lst))
file.close()
