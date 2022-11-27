file = open('C:/Study/pp1/07-FileHandling/During class/shoping.txt','a')

while True:
    groceries  = input(":")
    if groceries == "":
        break
    file.write(f"{groceries}\n")
    

file.close()