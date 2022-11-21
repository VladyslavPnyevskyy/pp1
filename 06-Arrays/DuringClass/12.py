lst = [[2,5,4],[9,0,3]]

#a.
print(lst)

#b.
rows = len(lst)
columns = len(lst[0])
print(rows,columns)

#c.
print(lst[0][1])

#d.
print(lst[1][2])

#e.
for x in range(0,len(lst[1])):
    print(lst[1][x], end=" ")
print()
#f.

for i in range(0,len(lst)):
    for x in range(0,len(lst[0])):
        print(lst[i][x], end=" ")
    print()    

#g.
for i in range(0,len(lst)):
    print(lst[i][2])