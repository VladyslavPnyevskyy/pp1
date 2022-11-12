for x in range(1,31):
    if x%3==0 and x%5==0:
        print("bingo", end = " ")
    elif x %5 ==0:
        print("five", end = " ")
    elif x % 3 ==0:
        print("three", end = " ")
    else:
        print(x, end = " ")
