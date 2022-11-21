lst = [5,1,9,6,1]
x = 0
y = 0
for i in lst:
    if i > x:
        y = x
        x = i
    elif i>y:
        y = i
print(y)
        