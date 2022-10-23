#for i in range(6,-1,-3):
 #   for j in range(1,4):
  #      print(f' {i+j}',end='')
   # print()

i = 9 
j = 2
while i > 0:
    while j > -1:
        print(f"{i-j}", end=" ")
        j =j - 1
    print()
    j = j + 3
    i = i - 3