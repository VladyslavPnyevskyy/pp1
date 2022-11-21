lst = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
for i in lst:
    for j in i:
        print("{:2d}".format(j), end = " ")
    print()
lst[0],lst[2]=lst[2],lst[0]
for i in lst:
    for j in i:
        print("{:2d}".format(j), end = " ")
    print()