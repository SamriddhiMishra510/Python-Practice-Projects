#Ask the user for a string and print out whether this string is a palindrome or not.
#  (A palindrome is a string that reads the same forwards and backwards.)

user_str = input("Please enter a word or a line:")
user_string_normalised = "".join(user_str.split()).lower()
print(f"The line {user_str} is","a" 
      if user_string_normalised==user_string_normalised[-1:-(len(user_str)+1):-1] 
      else "not a","palindrome")