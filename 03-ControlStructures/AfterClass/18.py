x = int(input("enter number: "))
cross5 = 0
cross2 = 0
cross1 = 0

if x % 5 == 0 :
    cross5 = x//5
else:
    cross5 = x//5
    if (x%5)%2 == 0:
        cross2 = (x%5)//2
    else:
        cross2 = (x%5)//2
        cross1 = (x%5)%2

print(f"5zł: {cross5}\n2zł: {cross2}\n1zł: {cross1}")