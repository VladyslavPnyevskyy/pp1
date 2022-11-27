import random

with open('C:/Study/pp1/07-FileHandling/After class/int20.txt', 'a') as file:
    for i in range(50):
        x = random.randint(100,999)
        xStr = str(x)
        file.write(f'{xStr}\n')