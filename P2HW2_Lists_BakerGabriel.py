# CTI-110
# P2HW2 - List
# Gabriel Baker
# 10/20/22
#
#
# ***************Pseudocode***************
# Input and display test grades for module 1
# Input and display test grades for module 2
# Input and display test grades for module 3
# Input and display test grades for module 4
# Input and display test grades for module 5
# Input and display test grades for module 6
# Create testGrades, variable for all grades combined
# 
# 
# 
# 
# 
# 
#*****************************************

module1 = float(input("Enter Grade for Module 1: "))
module2 = float(input("Enter Grade for Module 2: "))
module3 = float(input("Enter Grade for Module 3: "))
module4 = float(input("Enter Grade for Module 4: "))
module5 = float(input("Enter Grade for Module 5: "))
module6 = float(input("Enter Grade for Module 6: "))

testGrades = [module1, module2, module3, module4, module5, module6]

print("------------Results------------")
print(f'{"Lowest Grade: ":20s}{min(testGrades):.1f}')
print(f'{"Highest Grade: ":20s}{max(testGrades):.1f}')
print(f'{"Sum of Grades: ":20s}{sum(testGrades):.1f}')
print(f'{"Average: ":20s}{((sum(testGrades)) / 6):.2f}')
print("-------------------------------")





