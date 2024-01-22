# 1 The Hashtag Generator- 5kyu
# Training on The Hashtag Generator | Codewars

# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.


def generate_hashtag(s):
    # Check to see if string is empty return False

    if not s:
        return False
    
    # Capitalize each word and add a hashtag, remove spaces

    formatted_str = '#' + ''.join(word.capitalize() for word in s.split())

    # Check if the length of exceeds 140 characters return False

    if len(formatted_str) > 140:
        return False
    
    # Return the formatted string

    return formatted_str

input_string = "lets go for a walk down memory lane"
result = generate_hashtag(input_string)



#2 Sort my textbooks 8kyu
# Training on Sort My Textbooks | Codewars

# HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.
# The sorting should NOT be case sensitive (x.lower for case sensitive)

def sorter(textbooks):
    textbooks.sort(key=lambda x: x.lower())
    return textbooks



#3 Double Char 8kyu
# Training on Double Char | Codewars

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# char = character

def double_char(s):
    # Double each character in the string
    result_string = ''.join(char * 2 for char in s)
    return result_string



#4 Returning Strings 8kyu
# Training on Returning Strings | Codewars

# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    input_string = f"Hello, {name} how are you doing today?"
    return(input_string)



# #5 Square(n) Sum
# Training on Square(n) Sum | Codewars

# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 12+22+22=9
# 12+22+22=9

def square_sum(numbers):
    return sum (x**2 for x in numbers)
