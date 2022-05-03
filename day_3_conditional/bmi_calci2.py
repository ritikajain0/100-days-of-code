height = float(input("what is your height? "))
weight = float(input("what is your weight? "))
bmi= weight/(height*height)
bmi = round(bmi,2)
if bmi<18.5:
    print(f"your bmi is {bmi}, and you are underwight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("overweight")
elif bmi<35:
    print("obese")
else:
    print("clinically obese")