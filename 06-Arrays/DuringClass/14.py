lst = [[True,False],[True,True],[False,False]]
x=0
 
for i in lst:
    y = 0
    for j in i:
        
        if j==True:
            lst[x][y] = False
        else:
            lst[x][y] = True
        
        y = y+1 
        
    x = x + 1
print(lst)