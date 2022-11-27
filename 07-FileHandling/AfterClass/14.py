def numberOfLines(fileName):
    strFileName = str(fileName)
    with open(strFileName, 'r') as file:
        x = 0
        for line in file:
            x = x + 1
    print(f"Number of lines: {x}")
numberOfLines('C:/Study/pp1/07-FileHandling/During class/countries.txt')

