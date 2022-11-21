lst = [15, 8, 31, 47, 2, 19]
print(lst)
lst.reverse()
print(lst)
lst1 = [15, 8, 31, 47, 2, 19]
print(lst1)
x  = len(lst1)
for i in range(0,x):
    lst1[i] = lst1[x-1-i]
print(lst1)