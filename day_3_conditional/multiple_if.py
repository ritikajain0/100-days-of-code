#program to check is a user's height > 120 and if he is >=18 then he will pay 12$ else 7$
#this is a modified program where we ask user if they want photo then it will be addextra 3$ to their bill
height = int(input("what is your height? "))
age = int(input("what is your age? "))
bill=0
if height>120 :
    if age<12:
        bill=5
        print("your ticket is $5.")
    elif age<=18:
        bill=7
        print("your ticket is 7$")
    else:
        bill=10
        print("your ticket is 10$.")
    ans = input("do you want a photo yes/no ? ")
    if ans == "yes":
        bill+=3
    print(f"your total bill is {bill}$.")
    

else:
    print("you are not allowed to ride.")