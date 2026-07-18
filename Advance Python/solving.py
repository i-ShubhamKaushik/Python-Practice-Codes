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


# 2. Write a program to print third, fifth and seventh element from a list using enumerate 
# function. 

numbers = [1,2,3,4,5,6,7,8,9,0]
for i, number in enumerate(numbers):
    if i==2 or i==4 or i==6:
        print(number)


# 3. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number. 

n = int(input("Enter number: "))

list = [n*i for i in range(1,11)]
print(list)


# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’. 
try:
    num1= int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Can't divide a number by zero")
    

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

with open("Advance Python - 1/tables.txt", "a") as f:
    f.write(f"Table of {n} : {str(list)}\n")          #linked with question no. 3


# 6. Give an example of walrus.

if (n:= len([1,3,42,2,0])) > 4:
    print(f"List is too long ({n} elements, expected <=4)")