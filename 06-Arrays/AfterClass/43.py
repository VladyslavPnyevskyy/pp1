def identitymatrix(n):
    lst=[[0]*n for i in range(n)]
  
    for i in range(0,len(lst)):
        lst[i][i] = 1
        
    for i in lst:
        for j in i:
            print("{:2d}".format(j), end = " ")
        print()
identitymatrix(5)
identitymatrix(3)
identitymatrix(8)
