# CTI-110
# P3HW2 - MealTipTax
# Simba Varela
# 6/28/22
#


cost = float(input("Please enter cost of meal: "))

tip = float(input("Enter tip amount of 15, 18, or 20: "))

if tip == 15 or tip == 18 or tip == 20:
    tipAmount = cost * (tip/100)
    taxAmount = cost * .06
    totalAmount = cost + tipAmount + taxAmount
else:
    print("error")

print("Meal price: ",format(cost,',.2f'),'.')
print('Tax: :', taxAmount)
print('Tip: ', tipAmount)
print('Total: ', totalAmount)
