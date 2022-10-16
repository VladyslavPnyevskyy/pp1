NumberInput = input("wprowadź liczbę pomiędzy 0 i 1: ")
try:
    Number = float(NumberInput)
    if Number>1:
        print("Niepoprawna wartość")
    elif Number>=0.9:
        print("5,0")
    elif Number>=0.8:
        print("4,5")
    elif Number>=0.7:
        print("4,0")
    elif Number>=0.6:
        print("3,5")
    elif Number >=0.5:
        print("3,0")
    elif Number<0:
        print("Niepoprawna wartość")
    else: 
       print("2.0")

except: 
    print("wprowadź liczbe")





