#Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

#Extras:

#Instead of printing the elements one by one, make a new list that has all the elements 
# less than 5 from this list in it and print out this new list.

#Write this in one line of Python.

#Ask the user for a number and return a list that contains only elements from the 
# original list a that are smaller than that number given by the user.

#Main exercise
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in a:
    if item<5:
        print(item)

#Bonus 1 and 2
print([item for item in a if item<5])

#Bonus 3
user_number = float(input("Please enter a number:"))
print([item for item in a if item<user_number])


#Trial: program with exceptions considered.
retry=True
while retry:
    try:
        user_number = float(input("Please enter a number:"))
    except ValueError:
        print("Error: input given is not a number. Try again.")
    else:
        retry=False
else:
    less_than_user_number = [item for item in a if item<user_number]
    print(f"List of numbers in list a less than {user_number} is {less_than_user_number}")



