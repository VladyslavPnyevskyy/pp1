Name = input("enter your name: ")
Surname = input ("enter your surname: ")
print("Hello "+ Name, Surname)

CurentYearInput = input("What is curent year?: ")
UserBornYearInput = input("What year did you born? :")
CurentYear = int(CurentYearInput)
UserBornYear = int(UserBornYearInput)
UserAge = CurentYear - UserBornYear
print("you are", UserAge )