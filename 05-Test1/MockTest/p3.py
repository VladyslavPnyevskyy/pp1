def f(amount_to_pay):
    if amount_to_pay%5==0:
        return(amount_to_pay/5)
    else:
        if (amount_to_pay%5)%2 == 0:
            return((amount_to_pay//5)+((amount_to_pay%5)/2))
        else:
            return((amount_to_pay//5)+((amount_to_pay%5)//2)+(amount_to_pay%5)%2)




