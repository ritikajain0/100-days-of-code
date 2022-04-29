# program to add digits of a given no eg if no is 26 o/p is 2+6 = 8
num = input("type a two-digit-no\n")
no = int(num)
rem= no %10
no=no/10  # reminder divide always gives floating point

print(int(rem)+int(no))

#second method 

first_digit= int(num[0])
second_digit = int(num[1])
print(first_digit + second_digit)
