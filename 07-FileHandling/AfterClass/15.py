def displaylines(fileName):
   # strFileName = str(fileName)
    with open(fileName, 'r') as file:
        display = input(":")
        if display == "":
            x= 0
            for i in file:
                print(i)
                x = x + 1
                if x % 5 == 0:
                    display = input(":")
                    if display == "":
                        continue
                    else:
                        break
        


                    
            
displaylines('C:/Study/pp1/07-FileHandling/During class/shoping.txt')



