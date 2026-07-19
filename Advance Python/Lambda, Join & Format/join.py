# ========================================
# JOIN() PRACTICE QUESTIONS
# ========================================

# Q1. Given a list:

names = ["Shubham", "Rahul", "Aman", "Riya"]

# Join all the names into a single string separated by commas.
# Expected Output:
# Shubham, Rahul, Aman, Riya

print(", ".join(names))



# Q2. Given a string:

word = "PYTHON"

# Join each character using a hyphen (-).
# Expected Output:
# P-Y-T-H-O-N

print("-".join(word))



# Q3. Given a list of integers:

numbers = [10, 20, 30, 40]

# Convert all numbers into strings and join them using a single space.
# Expected Output:
# 10 20 30 40

print(" ".join(map(str,numbers)))



# Q4. Take 5 words as input from the user.
# Store them in a list and join them using " | ".
# Example Output:
# apple | banana | mango | grapes | orange

fruits = []

x= input("Enter fruit name: ")
fruits.append(x)
x= input("Enter fruit name: ")
fruits.append(x)
x= input("Enter fruit name: ")
fruits.append(x)
x= input("Enter fruit name: ")
fruits.append(x)
x= input("Enter fruit name: ")
fruits.append(x)

print(" | ".join(fruits))



# Q5. Take a sentence as input from the user.
# Reverse every individual word and join them back with spaces.
# Example:
# Input:
# Python is awesome
#
# Output:
# nohtyP si emosewa

sentence = input("Enter sentence: ")

result = " ".join(word[::-1] for word in sentence.split())

print(result)

