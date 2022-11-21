fhand = open('C:/Study/pp1/06-Arrays/BeforeClass/romeo.txt')
def wordToList(file):
    lst = []
    for line in file:
        line = line.rstrip()
        words = line.split()
        for word in words:
            if word not in lst:
                lst.append(word)
    lst.sort()
    print(lst)

wordToList(fhand)