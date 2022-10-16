lst = []

while True:
    numberInput = input("wprowadź liczbe: ") 
    if numberInput == "gotowe":
            break

    try:
         number = int(numberInput)
         lst.append(number)
    except:
        print("błędne wprowadzenie")
        
    
numberSum = sum(lst)
numberLen = len(lst)
arithmeticAverage = numberSum/numberLen

print(numberSum, numberLen, arithmeticAverage )

