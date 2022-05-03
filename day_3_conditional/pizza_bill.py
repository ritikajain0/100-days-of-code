size  = input("what pizza size you want s,m,l ? ")
add = input("do you want peppreoni y or n ? ")
cheese = input("do you want extra cheese y or n? ")
bill = 0
if size=='s':
    bill = 15
    if add=='y':
        bill+=2
elif size=='m':
    bill= 20
    if add=='y':
        bill+=3
else:
    bill=25
    if add=='y':
        bill+=3
if cheese=='y':
    bill+=1
print(f"your total bill is {bill}$.")