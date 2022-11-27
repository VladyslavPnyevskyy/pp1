import re

with open('C:/Study/pp1/07-FileHandling/After class/ToBeOrNotToBe.txt','r') as file:
    fileContent = file.read()
    m = re.findall('[a-zA-z]{6,}',fileContent)
    for i in m:
        print(i)