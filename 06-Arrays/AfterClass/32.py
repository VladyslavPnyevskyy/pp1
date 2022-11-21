def arrayToStr(array):
    counter = 0
    print(array)
    for i in array:
        counter = counter+1
        if counter == len(array):
            iStr = str(i)
            print(iStr)
        else:
            iStr = str(i)
            print(iStr, end=", ")
arrayToStr([5,4,3,2,6,5])   