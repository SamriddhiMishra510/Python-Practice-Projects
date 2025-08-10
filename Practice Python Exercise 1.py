#Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
# If you want to do this in a generic way, see exercise 39.
#Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


from datetime import date

current_year = int(date.today().year)
user_name = input("Please enter your name here:")
user_age = int(input("Please enter the age you turned this year:"))
year_turn_100 = current_year + 100 - user_age
verb = "will be" if user_age <= 100 else "were" 
print(f"{user_name}, you {verb} 100 in the year {year_turn_100}")
random_no = int(input("Please enter a random number:"))
print(f"{user_name}, you {verb} 100 in the year {year_turn_100} \n"*random_no)