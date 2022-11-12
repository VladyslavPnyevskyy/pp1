def f(cardNumber):
    hideCardNumber = str(f"{cardNumber[0:2]}**********{cardNumber[12:16]}")
    #print(hideCardNumber)
    return hideCardNumber

