lst = [1,2,3,4,5]

#a.
lst[0]  =lst[0]-1
print(lst)
#b.
lst[(len(lst)-1)]=lst[(len(lst)-1)]+4
print(lst)
#c.
lst[(len(lst)-1)//2]=lst[(len(lst)-1)//2]*2
print(lst)
#d.
for i in range(len(lst)):
    lst[i]=lst[i]+3
print(lst)