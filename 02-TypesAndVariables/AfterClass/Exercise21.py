import random


x=1
y=6
dise = random.randint(x,y)
guesInput = input("gues number between 1 and 6\n")
gues = int(guesInput)
print(dise==gues)