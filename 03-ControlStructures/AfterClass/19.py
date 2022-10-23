try :
    hummanAge = int(input("Enter the dog's age in human years: "))

    if hummanAge<= 2 :
        dogAge = hummanAge*10.5
        print(f"The dog's age in dog’s years is {dogAge} years.")
    else :
        dogAge = int((2*10.5)+(hummanAge-2)*4)
        print(f"The dog's age in dog’s years is {dogAge} years.")
except:
    print("wrong enter")

