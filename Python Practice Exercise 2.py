#Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

#Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number 
# to divide by (check). 
# If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message.

#Base exercise
user_number = int(input("Enter a random integer:"))
print(f"{user_number} is", "even" if user_number%2==0 else "odd")

#Bonus 1
if user_number%2==0:
    print(
        f"{user_number} is even and", "divisible by 4" 
        if user_number%4==0 
        else "not divisible by 4" 
        )
else: 
    print(f"{user_number} is odd")

#Bonus 2
user_input_numbers = input("Enter any two numbers separated by comma, second number being non-zero:")
numbers_given_list = user_input_numbers.split(",")
while len(numbers_given_list)!=2:
    print("Please enter exactly two numbers, separated by a comma")
    user_input_numbers = input("Enter any two number separated by a comma, second number being non-zero:")
    numbers_given_list = user_input_numbers.split(",")
else:
    num, check = numbers_given_list
while int(check)==0:
    print("Second number should be non-zero")
    user_numbers = input("Enter any two number separated by comma, second number being non-zero:")
    num, check = user_numbers.split(",")
else:
    print(f"{num} is divisible by {check}" if int(num)%int(check)==0 else f"{num} is not divisible by {check}")
    
