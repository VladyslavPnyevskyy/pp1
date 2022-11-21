lst = [[0,0,0],[0,0,0],[0,0,0]]
x = 0
y = 0
for i in lst: 
    for j in i:
        lst[x][y] = 1
    x = x + 1
    y = y + 1
print(lst)
            
