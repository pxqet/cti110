# CTI-110
# P2HW2 - List and Sets
# Simba Varela
# 6/16/21
#


mylist=[]

num = float(input("Enter num 1:"))
mylist.append(num)
num = float(input("Enter num 2:"))
mylist.append(num)
num = float(input("Enter num 3:"))
mylist.append(num)
num = float(input("Enter num 4:"))
mylist.append(num)
num = float(input("Enter num 5:"))
mylist.append(num)
num = float(input("Enter num 6:"))
mylist.append(num)
print()
print('created list')
print(mylist)

print("smallest number in list",min(mylist))
print("Largest number in list",max(mylist))

print("sum of numbers in list:",sum(mylist))

print("average of numbers in list:",sum(mylist)/len(mylist))
print()
print('created set')
print(set(mylist))
