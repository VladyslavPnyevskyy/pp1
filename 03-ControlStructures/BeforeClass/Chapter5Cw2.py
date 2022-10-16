lst=[]

while True :
    numberInput = input("wprowadź liczbe: ")

    if numberInput == "gotowe" :
        break

    try :
        number = float(numberInput)
        lst.append(number)
    except : 
        print("błędne wprowadzenie")
    
def max(lst):
    largest = None
    for num in lst:
        if largest is None or num > largest :
            largest = num
    print(largest)

def min(lst):
    smalest = None
    for num in lst:
        if smalest is None or num < smalest :
            smalest = num
    print(smalest)
    
max(lst)
min(lst)