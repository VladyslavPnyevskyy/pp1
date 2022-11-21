lst = [2, 3, 2, 5, 8, 1, 9, 8]

for i in lst:
    counter = 0
    for j in lst:
        if i == j:
            counter = counter + 1 
    if counter==1:
        print(i, end = " ")

