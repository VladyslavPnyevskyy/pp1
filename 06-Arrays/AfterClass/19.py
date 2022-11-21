lst = [15, 8, 31, 47, 2, 19]
x = 0
y = 0
while len(lst)>x:
    y = y + lst[x]
    x = x + 1
    
print(lst)
print(y/x)
print(sum(lst)/(len(lst)))
print(len(lst))