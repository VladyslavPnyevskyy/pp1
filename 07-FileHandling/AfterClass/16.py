with open('C:/Study/pp1/07-FileHandling/During class/shoping.txt', "r") as file:
    with open('C:/Study/pp1/07-FileHandling/During class/copy.txt', 'a') as copy:
        file_content = file.read()
        copy.write(file_content)