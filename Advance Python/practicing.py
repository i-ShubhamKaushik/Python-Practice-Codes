# 1. Walrus Operator

# Give an example of walrus.

if (n:= len([1,3,42,2,0])) > 4:
    print(f"List is too long ({n} elements, expected <=4)")

# Write a program that keeps asking the user to enter a number until they enter a number greater than 100. Use the walrus operator (:=) instead of writing input() separately.

while True:
    if (n:= int(input("Enter a number: "))) > 100:
        break



# 2. Type Hints

# Create a function calculate_area(length, width) using type hints. It should return the area of a rectangle. Test it with integer and float values.

def calculate_area(length: float, width: float)->float:
    return length*width

print(calculate_area(1,2))


def calculate_area(length: int, width: int)->int:
    return length*width

print(calculate_area(1,2))



# 3. Match-Case

# Write a calculator program using match-case that performs:

# Addition
# Subtraction
# Multiplication
# Division

# Take the operator (+, -, *, /) from the user.


def calculator(a, b):
    oper= input("Your operator (+, -, *, /): ")

    match oper:
        case "+":
            print(f"{a}+{b}= {a+b}")
        case "-":
            print(f"{a}-{b}= {a-b}")
        case "/":
            if b ==0:
                raise ZeroDivisionError("Can't divide by zero brooo")
            else:
                print(f"{a}/{b}= {a/b}")
        case "*":
            print(f"{a}*{b}= {a*b}")

calculator(2,6)



# 4. Dictionary Merge

# Given:

student = {"name": "Shubham", "age": 18}
marks = {"python": 95, "math": 87}

# Merge both dictionaries using the | operator and print the result.

merged = student|marks
print(merged)



# 5. Dictionary Update Operator

# Create two dictionaries containing product information and use |= to update the first dictionary with the second one.

product1 = {
    "name": "Laptop",
    "price": 50000
}

product2 = {
    "brand": "Lenovo",
    "stock": 10
}

product1 |= product2

print(product1)



# 6. Exception Handling

# Ask the user to enter two numbers and perform division.
# Handle:

# Invalid input
# Division by zero

# Print a custom error message for both cases.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a/b)

except ValueError:
    print("Enter a valid number: ")
except ZeroDivisionError:
    print("Can't divide by zero")



# 7. Global Keyword

# Create a global variable count = 0.
# Write a function that increases it by 1 every time the function is called using the global keyword.

# Call the function five times.

x = 0

def count():
    global x
    x +=1

count()
count()
count()
count()
count()

print(x)



# 8. Enumerate

# Given:

languages = ["Python", "Java", "C++", "JavaScript", "Go"]

# Print the output as:

# 1. Python
# 2. Java
# 3. C++
# ...

# using enumerate().

for index, language in enumerate(languages, start=1):
    print(f"{index}. {language}")



# 9. Write a program to print third, fifth and seventh element from a list using enumerate 
# function. 

numbers = [1,2,3,4,5,6,7,8,9,0]
for i, number in enumerate(numbers):
    if i==2 or i==4 or i==6:
        print(number)



# 10. List Comprehension

# Given:

numbers = [1,2,3,4,5,6,7,8,9,10]

# Use list comprehensions only.

# Create:

# A list of all even numbers.

even = [num for num in numbers if num %2==0]
print(even)

# A list of squares of numbers greater than 5.

squares = [num**2 for num in numbers if num>5]
print(squares)



# 11. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number. 

n = int(input("Enter number: "))

list = [n*i for i in range(1,11)]
print(list)



# 12. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

with open("Advance Python/tables.txt", "a") as f:
    f.write(f"Table of {n} : {str(list)}\n")          #linked with question no. 11