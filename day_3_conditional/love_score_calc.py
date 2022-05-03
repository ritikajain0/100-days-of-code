#this is a program to calculate love score
# by calculating no of char in "true love" appears in both the names given by user
name1 = input("type name1 : ")
name2 = input("type name2 : ")
name1= name1.lower()
name2 = name2.lower()
t = name1.count("t")+ name2.count("t")
r = name1.count("r")+ name2.count("r")
u = name1.count("u")+ name2.count("u")
e = name1.count("e")+ name2.count("e")
l = name1.count("l")+ name2.count("l")
o = name1.count("o")+ name2.count("o")
v = name1.count("v")+ name2.count("v")
true = t+r+u+e
love = l+o+v+e
love_score = (true*10)+love
if love_score<10 or love_score>90:
    print(f"your love score is {love_score}, you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
    print(f"your love score is {love_score}, you are alright together")
else:
     print(f"your love score is {love_score}")

# we can also first combine string like combined_str=name1+name2
