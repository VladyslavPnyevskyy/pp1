from math import remainder


HeightInCmInput = input("Enter your height:\n")
HeightInCm = int(HeightInCmInput)
HeightInInches = HeightInCm//2.54
HeightInFeet = HeightInInches//12
remainder = HeightInInches%12
#print(HeightInFeet)
print(f"your height is {HeightInCm} cm tall, i.e. {HeightInFeet} feet and {remainder} inches.")