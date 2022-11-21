lst = [1,4,6,8,3,9,2]
n = len(lst)
for i in range(0,n):
    for j in range(0,n-i-1):
        if lst[j]%2!=0 and lst[j+1]%2==0:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)