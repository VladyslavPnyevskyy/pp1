xStr = input(":")
x = int(xStr)
lst = [1,4,8,13,52]
counter = 0
for i in lst:
    if i>x:
        counter = counter + 1

print(counter)
