# Warm up: Basic output with variables
# Sep 25, 2022
# P1HW1Output
# Gabriel Baker
#
# ****************  Pseudocode ****************
# Display "Enter integer:" 
# Input integer
# Display user_num "squared is", then square user_num
# Display cubing of user_num
# Display "Enter another integer:"
# Display addition of first and second integer
# Display multiplication of first and second integer

user_num = int(input('Enter integer:\n'))
print('You entered:' , user_num)
print(user_num , 'squared is' , user_num * user_num)
print('And' , user_num , 'cubed is' , user_num * user_num * user_num, '!!')
user_num2 = int(input('Enter another integer:\n'))
print(user_num , '+' , user_num2 , 'is' , user_num + user_num2)
print(user_num , '*' , user_num2 , 'is' , user_num * user_num2)
