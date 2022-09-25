# Program for calculating travel expenses
# 9/25/22
# CTI-110 P1HW2 - Travel Expense
# Gabriel Baker
# 
# *************** Pseudocode ***************
# Display "This program calculates and displays travel expenses"
# Displays "Enter Budget:" and allows input of budget
# Displays "Enter your travel destination:" and allows input of destination
# Displays "How much will you spend on gas?" and allows input of gas
# Displays "How much will you spend on your accomodations?" and allows accomodations input
# Displays "How much will you spend on food" and allows input
# Expenses equation
# Remaining balance equation 
# Print all gathered information and add its amounts
# Print remaining balance equation

print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much will you spend on gas? "))
accomodations = int(input("How much will you spend on your accomodations? "))
food = int(input("How much will you spend on food? "))
expenses = gas + accomodations + food
RemainBal = budget - expenses
print("----------Travel expenses----------")
print("Location: " , destination)
print("Initial Budget: " , budget)
print("Gas: " , gas)
print("Accomodations: " , accomodations)
print("Food: " , food)
print("Remaining Balance: " , RemainBal)

