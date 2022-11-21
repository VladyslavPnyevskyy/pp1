lst=[1,2,3,4,5,6,7]
x=0
odd = 0
even = 0
while x<len(lst):
    if lst[x]%2==0:
        even = even+1
    if lst[x]%2 != 0:
        odd = odd+1
    x = x+1
print(even,"parystych")
print(odd,"nie parzystych")