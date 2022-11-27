with open('C:/Study/pp1/07-FileHandling/During class/shoping.txt', "r") as file:
    with open('C:/Study/pp1/07-FileHandling/During class/copy.txt', 'a') as copy:
        for i in file:
            copy.write(i)