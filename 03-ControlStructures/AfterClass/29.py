lst = []
x = None


while x != 0:
    
    x = int(input("Enter number: "))
    if x != 0:
        lst.append(x)

print(f"RESULT: Quantity={len(lst)},Sum={sum(lst)}, Mean={sum(lst)/len(lst)}")
