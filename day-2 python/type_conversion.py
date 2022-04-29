# to check data type of any variable
no_char = len(input("what is your name?"))
print(type(no_char))       #print datatype of num_char variable which is int returned by len function

# this will give error bcz no_char is int type ---  print("your name has" + no_char +"characters.")
#type conversion
new_no_char= str(no_char)
print("your name has " + new_no_char +" characters.")

a=100
print(70 + a)
print(70 + float(a))
print("70" + str(a))

#imp round function
print(round(8/3))

# also we can specify no at which we want toround off
print(round(8/3 ,2))

#also we can convert directly floating result to int
print(8//3)
print(type(8 // 3))  # int data type
