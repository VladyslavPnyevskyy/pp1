import random
x = random.randint(1,50)
xStr = str(x)
with open('C:/Study/pp1/07-FileHandling/After class/int19.txt', 'a') as file:
    file.write(xStr)