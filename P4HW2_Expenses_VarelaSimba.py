# CTI-110
# P4HW2 - Expenses
# Your Name
# 7/7/22

#enter an starting amount in account

amount = float(input("Enter starting amount in account $"))

keep_going = "y"
total = 0
count = 0
while keep_going.lower() == "y":
    print()
    count +=1
    expense = float(input('Enter expense ' +str(count) + ": "))
    total += expense
    keep_going = input ('Do you want to enter another expense?(y/n) ')
    print()
subtracted_amount = amount - total
print('Amount in accout before expenses subtracted $',amount)
print('Number of expenses entered: ',count)
print('Amount in account After expenses subtracted is $', subtracted_amount)
