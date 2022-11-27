with open('C:/Study/pp1/07-FileHandling/After class/int21.txt', 'a') as file:
    for i in range(1,11):
        file.write(f"{i}, {i**2}, {i**3}\n")