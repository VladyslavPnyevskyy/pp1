import math

aInput = input("Print a:\n")
a = int(aInput)

bInput = input("Print b:\n")
b = int(bInput)

cInput = input("Print c:\n")
c = int(cInput)

s = (a+b+c)/2
A = s*(s-a)*(s-b)*(s-c)
Area = math.sqrt(A)
print("Area is:{Area} squer cantimiters")
