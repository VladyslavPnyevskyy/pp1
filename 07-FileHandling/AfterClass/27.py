import re
with open('C:/Study/pp1/07-FileHandling/After class/grades.txt','r') as file:
    lst = []
    fileContent = file.read()
    m = re.findall('\d.\d', fileContent)
    for i in m:
        iFloat = float(i)
        lst.append(iFloat)
    print(sum(lst)/len(lst))
