# CTI-110
# P4HW1 - Score List
# Simba Varela
# 7/5/22
#


def main():
    #print('Main Function')
    grade=0
    total=0
    grade_list=[]
    print(grade_list)
    num=int(input('How many scores do you want to enter: '))
    #print(num)
    for i in range(0,num):
        grade=float(input('Enter score #'+str(i+1)+': '))
        while grade <0 or grade>100:
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            grade=float(input('Enter score #'+str(i+1)+': '))
        grade_list.append(grade)
    #print(grade_list)
    lowest=min(grade_list)
    #print(lowest)
    grade_list.remove(lowest)
    #print(grade_list)
    average=sum(grade_list)/len(grade_list)
    #print(average)
    if average >=90:
        letter="A"
    elif average >=80:
        letter="B"
    elif average >=70:
        letter="C"
    elif average >=60:
        letter="D"
    else:
        letter="F"
    print('----------Results----------')
    print('Lowest Score:   ',lowest)
    print('Modified List:  ', grade_list)
    print('Scores Average: ',format(average,",.2f"))
    print('Grade:          ', letter)
        
main()

