#program to check is a user's height > 120 and if he is >=18 then he will pay 12$ else 7$
height = int(input("what is your height? "))
age = int(input("what is your age? "))
if height>120 :
    if age<12:
        print("please pay $5.")
    elif age<=18:
        print("please pay 7$")
    else:
        print("please pay 10$.")
else:
    print("you are not allowed to ride.")