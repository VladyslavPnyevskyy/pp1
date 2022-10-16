

try:
    HourInput = input("podaj liczbe godzin: ")
    Hour = float(HourInput)
    IndexInput = input("podaj stawke godzinową: ")
    Index = float(IndexInput)
    if Hour>40:
        Earnings = 40*Index + (Hour-40)*(Index*1.5)
    else :
        Earnings = Hour * Index
    print(f"Wynagrodzenie: {Earnings}")
except:
    print("Błąd, podaj wartość numeryczną")


