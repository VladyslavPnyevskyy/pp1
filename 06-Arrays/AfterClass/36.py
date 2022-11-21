lst =  [[2,3,4,5],[6,7,98,9]]
for i in lst:
    for j in i:
        print("{:2d}".format(j), end = " ")
    print()