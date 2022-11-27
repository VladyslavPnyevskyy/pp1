file = open('C:/Study/pp1/07-FileHandling/During class/countries.txt')
x=1
for line in file:
    line = line.rstrip()
    print(f"{x}.{line}", end=" ")
    x=x+1
file.close()
