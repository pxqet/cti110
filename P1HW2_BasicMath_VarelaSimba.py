#IDLE MATH Programming
# 6/16/21
# CTI-110 P1HW2 - Basic Math
# Simba Varela
#


expense = input("Enter name of expense: ")
charge = float(input("Enter monthly charge: "))
tax = charge * .06
monthly_charge = charge + tax
annual_charge = monthly_charge * 12

print("Bill: " + expense + "-------- Before Tax: $",charge,sep='')
print("Monthly tax:     $",format(tax,',.2f'),sep='')
print("Monthly_charge:  $",format(monthly_charge,',.2f'),sep='')
print("annual_charge:   $",format(annual_charge,',.2f'),sep='')


