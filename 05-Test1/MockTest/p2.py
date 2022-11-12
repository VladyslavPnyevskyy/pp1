def f(binary_number):
    count = 0
    for letter in binary_number:
        if letter == "1":
            count = count + 1
        elif letter == "0":
            count = count + 1
        else:
            continue

    if count == len(binary_number):
       # print("true")
       return True
    else:
       # print("false")
       return False


