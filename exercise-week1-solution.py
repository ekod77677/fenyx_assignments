# Exercise-1 solution
from copy import copy


weight = float(input('Please enter your weigth: '))
height = float(input('Please enter your height: '))
Body_Mass_Index = weight / height ** 2
if Body_Mass_Index < 18.5:
    print("UNDERWEIGHT")
elif 18.5 >= Body_Mass_Index <= 25:
    print("NORMAL")
elif 25 >= Body_Mass_Index <= 30:
    print("OVERWEIGHT")
elif 30 >= Body_Mass_Index <= 35:
    print("OBESE")
elif Body_Mass_Index > 35:
    print("EXTREMELY OBESE")

# Exercise-2 solution
while True:
    name = str(input('What is your name: '))
    continues = input('Do you want to continue? y/n: ')
    if continues.lower() != "y":
        break
    print("Enter Marks Obtained in 4 assignment: ")
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    a4 = int(input())
    assign_scores = (a1 + a2 + a3 + a4) / 4
    continues = input('Do you want to continue? y/n: ')
    if continues.lower() != "y":
        break
    print("Enter Marks Obtained in 2 test: ")
    t1 = int(input())
    t2 = int(input())
    test_scores = (t1+t2) / 2
    continues = input('Do you want to continue? y/n: ')
    if continues.lower() != "y":
        break
    print("Enter Marks Obtained in 2 lab works: ")
    l1 = int(input())
    l2 = int(input())
    lab_work_scores = (l1+l2) / 2
    score = assign_scores * 10 / 100 + test_scores * 70 / 100 + lab_work_scores * 20 / 100
    print(score)
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    break







    
    
    

    
    
    