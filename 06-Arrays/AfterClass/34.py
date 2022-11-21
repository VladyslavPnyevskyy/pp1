lst = [1,2,3,4,7]
lst1 = [1,2,4,3,5,6,7,89,9]
counter = 0
for i in lst:
    if i in lst1:
        continue
    else:
        counter = counter +1 
if counter > 0:
    print(False)
else:
    print(True)

