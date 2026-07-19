# LAMBDA FUNCTIONS    
# Function created using an expression using ‘lambda’ keyword. 
# Syntax: 
# lambda arguments:expressions 
# can be used as a normal function 


# Example: 
square = lambda x:x*x 
print(square(6))  # returns 36 


sum = lambda a,b,c:a+b+c 
53 
print(sum(1,2,3)) # returns 6 


# ========================================
# LAMBDA FUNCTION PRACTICE QUESTIONS
# ========================================

# Q1. Write a lambda function that returns the square of a number.

square = lambda x:x*x
print(square(2))



# Q2. Write a lambda function that returns the larger of two numbers.

larger = lambda a,b: a if a>b else b

print(larger(23,12))



# Q3. Given:

numbers = [1, 2, 3, 4, 5]

# Use map() with a lambda function to double every element in the list.

double = lambda x: x*2

doubled_list = map(double, numbers)

print(list(doubled_list))



# Q4. Given:

numbers = [12, 7, 5, 20, 18, 3]

# Use filter() with a lambda function to create a new list containing only even numbers.

def even(n):
    if n%2==0:
        return True
    return False

even_list = filter(even, numbers)
print(list(even_list))



# Q5. Given:

students = [
    ("Rahul", 72),
    ("Shubham", 95),
    ("Aman", 81),
    ("Riya", 88)
]

# Use sorted() with a lambda function to sort the list according to marks in ascending order.

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)