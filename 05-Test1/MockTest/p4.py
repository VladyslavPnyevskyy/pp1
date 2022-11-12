def f( number, even):
    lst = []
    if even == True:
        stringNumber = str(number)
        for letter in stringNumber:
            intLetter = int(letter)
            if intLetter % 2 == 0:
                lst.append(intLetter)
    else:
        stringNumber = str(number)
        for letter in stringNumber:
            intLetter = int(letter)
            if intLetter % 2 != 0:
                lst.append(intLetter)
    result = sum(lst)
    return result

            
