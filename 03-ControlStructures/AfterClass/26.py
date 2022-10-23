pinCode = "0805"
x= 0
for i in range (5):
    
    pin = input("Enter the PIN code: ")
    if pin == pinCode:
        print("corect!")
        break
    else:
        x = x+1
        print("incorect...")
    
    if x == 3:
        print("Sorry, your payment card has been blocked.")
        break
