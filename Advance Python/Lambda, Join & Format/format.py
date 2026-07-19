# ========================================
# STRING FORMATTING PRACTICE QUESTIONS
# ========================================

# Q1. Use variables:

name = "Shubham"
age = 18
language = "Python"

# Print the following sentence using string formatting:
# My name is Shubham. I am 18 years old and learning Python.

format = "My name is {}. I am {} years old and learning {}.".format(name, age, language)
print(format)



# Q2. Given:

pi = 3.1415926535

# Print the value of pi rounded to 3 decimal places using formatting.

print("{:.3f}".format(pi))



# Q3. Given:

item = "Keyboard"
price = 899
quantity = 2

# Print the bill in the following format:
# Keyboard x 2 = ₹1798

bill = "{0} X {1} = ₹{2}".format(item, quantity, price*quantity)
print(bill)



# Q4. Print the following table using proper formatting so that the columns remain aligned.
#
# Name       Marks
# Shubham      95
# Rahul        87
# Rohit        91

aligned = '''
Name\t\tMarks
Shubham\t\t{}
Rahul\t\t{}
Rohit\t\t{}'''.format(95,87,91)

print(aligned)



# Q5. Create a report card using formatting.

# Variables:
name = "Aman"
math = 87
science = 92
english = 78

# Expected Output:
# Student : Aman
# Math    : 87
# Science : 92
# English : 78
# Average : 85.67

average = (math+science+english)/3

report_card = '''
Student\t\t{}
Math\t\t{}
Science\t\t{}
English\t\t{}
Average\t\t{}'''.format(name, math, science, english, average)

print(report_card)