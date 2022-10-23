a = int(input("enter a: "))
b = int(input("enter b: "))

for i in range(b):
    if i == 0 or i == b-1:
        for j in range (a):
            print("* ", end= "")
        print()
    else:
        for j in range(a):
            if j == 0 or j == a-1:
                print("* ", end="")
            else:
                print(end ="  ")
        print()





