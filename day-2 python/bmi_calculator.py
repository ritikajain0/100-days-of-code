#program to calculate bmi = weight/(height*height)
weight= float(input("type your weight in kg: "))
height= float(input("type your height in m : "))
bmi = weight / (height ** 2)
print(int(bmi))
