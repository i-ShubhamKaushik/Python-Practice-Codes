# Example:

try:
    age = int(input("Enter your age: "))
    print(f"your age is {age}")

except ValueError:
    print("Value Error: Age should be an integer")

finally:
    print("Final Statement")



#             Q U E S T I O N S 


# Divide Two Numbers
# Learn try, except
# Handle ValueError and ZeroDivisionError

try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a/b)
except ValueError as v:
    print("\nMust be an integer!")
except ZeroDivisionError as v:
    print("\nCannot divide with zero!")
finally:
    print("Program ended")

# Valid Integer Input
# Learn while + try/except
# Keep asking until the input is valid

while True:
    try:
        integer = int(input("\nEnter an integer: "))
        break
    except ValueError:
        print("\nMust be an integer")

# Safe List Access
# Practice IndexError
# Handle invalid index and invalid input

numbers = [0,1,2,3,4,5]

try:
    index = int(input("Enter index: "))
    print(numbers[index])
except IndexError:
    print(f"\nIndex : {index} - doesn't exist.")
except ValueError:
    print("\nIndex must be an integer!")

# File Reader
# Practice FileNotFoundError
# Good introduction to exception handling with file operations

try:
    file_name = input("\nEnter file name: ")
    with open(f"{file}", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\nThis file doesn't exist\n")


# Mini Calculator
# Combine everything you've learned:
# ValueError
# ZeroDivisionError
# Invalid operator
# Use try, except, else, and finally

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter Operation (*, /, +, -): ")

    if operation == "-":
        print(f"Result: {num1-num2}")
    elif operation == "+":
        print(f"Result: {num1+num2}")
    elif operation == "*":
        print(f"Result: {num1*num2}")
    elif operation == "/":
        print(f"Result: {num1/num2}") 
    else:
        print("Invalid Operation..!")

except ValueError:
    print("Number must be an integer!")
except ZeroDivisionError:
    print("Cannot divide any number with zero!")
else:
    print("Calculation completed successfully!")
finally:
    print("\nProgram Ended..!\n")



# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same. 

try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)



# 2. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’. 

try:
    num1= int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Can't divide a number by zero")