#Take two lists, say for example these two:
  #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements 
# that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python 

#Main exercise
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

intersection_a_and_b = []
for item in a:
    if item in b and item not in intersection_a_and_b:
        intersection_a_and_b.append(item)

print(intersection_a_and_b)

#Bonus 1
import random
len_list_1, len_list_2 = random.sample(range(0,50), 2)
list_1 = random.sample(range(-10000,10000), len_list_1)
list_2 = random.sample(range(-10000,10000), len_list_2)

intersection_of_lists = []
for item in list_1:
    if item in list_2 and item not in intersection_of_lists:
        intersection_of_lists.append(item)

print(list_1,list_2, intersection_of_lists, sep="\n")

#Bonus 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list({item for item in a if item in b}))