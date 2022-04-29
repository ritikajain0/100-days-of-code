# this is a challenge to calc remaining days,months ans weeks in your life if max we can live upto90 years using f_string

age = input("what isyour age ? ")
rem_age = 90 - int(age)

rem_month = rem_age * 12
rem_weeks = rem_age * 52
rem_days = rem_age * 365

print(f"you have {rem_month} months , {rem_weeks} weeks and {rem_days} days.")