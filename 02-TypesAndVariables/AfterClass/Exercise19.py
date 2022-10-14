HeightInput = input("Enter your height in cm\n")
WeightInput = input("Enter your weight in kg\n")
HeightInCm = int(HeightInput)
Weight = int(WeightInput)
Height = HeightInCm/100
Bmi = Weight/Height**2
print(f"BMI index: {Bmi}")