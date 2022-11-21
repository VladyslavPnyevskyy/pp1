lst = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
for i in lst:
    for j in i:
        print("{:2d}".format(j), end = " ")
    print()
print()
for i in range(0,len(lst)):
    lst[i][1],lst[i][4]=lst[i][4], lst[i][1]
for i in lst:
    for j in i:
        print("{:2d}".format(j), end = " ")
    print()