with open("C:/Study/pp1/07-FileHandling/After class/shopinglist.txt", 'a') as copy:
    with open('C:/Study/pp1/07-FileHandling/After class/GrainsAndBread.txt', 'r') as ffile:
        with open('C:/Study/pp1/07-FileHandling/After class/MeatAndFish.txt', 'r') as sfile:
            with open("C:/Study/pp1/07-FileHandling/After class/shopinglist.txt", 'a') as copy:
                ffileContent = ffile.read()
                sfileContent = sfile.read()
                copy.write(ffileContent)
                copy.write(sfileContent)