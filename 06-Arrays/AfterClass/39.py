lst = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
x = 1
y = 1
for j in range(0,len(lst)):
    lst[0][j]=x
    x= x+1
for i in range(0,len(lst)):
    lst[i][0]=y
    y = y + 1
for i in range(1,len(lst)):
    for j in range(1,len(lst[i])):
        lst[i][j]=lst[0][i]*lst[j][0]
for i in lst:
    for j in i:
        print("{:2d}".format(j), end = " ")
    print()