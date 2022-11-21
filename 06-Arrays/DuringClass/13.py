lst =  [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
summ = []
for i in lst:
    for j in i:
        if j%2==0:
            summ.append(j)
print(sum(summ))