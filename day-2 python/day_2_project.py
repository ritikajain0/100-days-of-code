# this is day 2 finalproject i.e tip calculator

total_bill = input("what is your total bill? ")
tip_perc = input("what percentage you want to give as tip 10 12 or 15 ? ")
no_of_people = input("how many persns to split the bill ? ")

new_total_bill= float(total_bill) + (int(tip_perc)/100)*float(total_bill)

each_bill = float(new_total_bill)/int(no_of_people)
each_bill = round(each_bill , 2)
print(each_bill)