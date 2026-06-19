#Create a nested dictionary to store details of two students.

# user_input = (input("Enter first subject:" ),
#              input("Enter second subject:" ),
#              input("Enter third subject:" ),
#             input("Enter fourth subject:" ),
#             input("Enter fifth subject:" ),
#              )

# typecast = set(user_input)

# print(len(typecast))


#Create a nested dictionary to store details of two students.

# Students_details = {
#     "student1" : {
#         "name" : "john", 
#         "class" : "5th grader",
#         "Marks" : 80
#     },
#     "student2" : {
#         "name" : "michael",
#         "class" : "5th grader",
#         "Marks" : 85
#     }
# }

# from itertools import count


# Count = 1
# while Count <= 5:
#     print("Hello World")
#     Count += 1

#     print(count)


# word = "programming"

# for char in word:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         print(char, "-> Vowel")

# def val_type(n):
#     if n%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#         print(val_type)

# val_type(3)
# val_type(8)


# def fact(n):
#     if (n==1 or n==0):
#         return 1
#     else:
#         return (n-1) * n

# print(fact(5))


# def print_table(n):
#     for i in range(1,11):
#         print(n*i)

# print_table(10)
# print_table(13)

# with open("file.txt", "w") as f:
#     f.write("I'm Shubham Kaushik")

# with open("file.txt", "a") as f:
#     f.write("\nI'm programming in python")

# with open("file.txt", "r") as f:
#     read = f.read()
#     print(read)

#     line1 = f.readline()
#     print(line1)

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#         s1 = student("Shubham", 18)

#         print(s1.name)
        # print(s1.age)


# class account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
    #     self.balance += amount
    #     print(f"Deposit successful. New balance: {self.balance}")

    # def withdraw(self, amount):
    #     if amount > self.balance:
    #         print("Insufficient funds.")
    #     else:
    #         self.balance -= amount
    #         print(f"Withdrawal successful. New balance: {self.balance}")

    #         acc1 = account("Shubham", 1000)
    #         acc1.deposit(500)
    #         acc1.withdraw(1200)



# with open("file.txt", "w") as f:
#     f.write("Hello World")

#     with open("file.txt", "r") as f:
#         read = f.read()
#         print(read)

# with open("script.txt", "w") as f:
#     f.write("1st script...")

#     with open("script.txt", "r") as f:
#         read = f.read()
#         print(read)


# with open("file.txt", "a") as f:
#     f.write("\nComatozze is the greatest actress ever existed!")

# with open("file.txt", "r") as f:
#     read = f.read()
#     print(read)

# print("Hello World")

# Marks = []
  
# list.append(int(input("Enter Marks: ")))
# list.append(int(input("Enter Marks: ")))
# list.append(int(input("Enter Marks: "))) 
# list.append(int(input("Enter Marks: ")))
# list.append(int(input("Enter Marks: ")))
# list.append(int(input("Enter Marks: "))) 
# list.append(int(input("Enter Marks: "))) 
# list.append(int(input("Enter Marks: "))) 


# print(list)


# set = set()
# set.add(int(input("Enter Marks: ")))
# set.add(int(input("Enter Marks: ")))
# set.add(int(input("Enter Marks: ")))
# set.add(int(input("Enter Marks: ")))
# set.add(int(input("Enter Marks: ")))
# set.add(int(input("Enter Marks: ")))
# set.add(int(input("Enter Marks: ")))
# set.add(int(input("Enter Marks: ")))

# print(set)

# set = {18, '18'}
# print(set)

# dict = {}

# name = input("Enter name: ")
# lang = input("Enter programming language: ")
# dict.update({name: lang})

# name = input("Enter name: ")
# lang = input("Enter programming language: ")
# dict.update({name: lang})

# name = input("Enter name: ")
# lang = input("Enter programming language: ")
# dict.update({name: lang})

# name = input("Enter name: ")
# lang = input("Enter programming language: ")
# dict.update({name: lang})

# print(dict)

# a = int(input("Enter number: "))

# if a>=18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# a = int(input("Enter age: "))

# if a >= 18 :
#     print("YES")
# else:
#     print("no")

# username = input("Enter username: ")

# if len(username) < 10:
#     print("Username must be at least 10 characters long.")
# else:
#     print("All is well!")

# WAP to find if a name exists ina list or not

# names = ["Shubham", "Michael", "John", "Emily", "Sarah"]
# name = input("Enter name: ")
# if name in names:
#     print("Name exists in the list.")
# else:
#     print("Name does not exist in the list.")


# grades = int(input("Enter marks: "))

# if grades >=90 and grades <=100:
#     print("Excellent")
# elif grades >= 80 and grades <90:
#     print("A")
# elif grades >= 70 and grades <80:
#     print("B")
# elif grades >= 60 and grades < 70:
#     print("C")
# elif grades >= 50 and grades < 60:
#     print("D")
# elif grades <50:
#     print("FAIL")

# post = input("Enter post: ")

# if "Shubh".lower() in post.lower():
#     print("Shubham is mentioned in the post. ")
# else:
#     print("SHUBHAM is not mentioned in the post.")

# i = 1
# while i <= 31545454545454545497:
#     print("Hello World", i)
#     i += 1 

# from builtins import len, print


# list = [1, 2, 3, 4, 5]

# i = 0

# while i < len(list):
#     print(list[i])
#     i += 1

# for i in range(10):
#     if (i == 5):
#         break
#     print(i)


# for i in range(10):
#     if (i==4):
#         continue
#     print(i)

# for i in range(10):
#     if (i==5):
#         pass
#     print(i)


# list = ["Shubham", "Soham", "Michael", "John", "Harry"]

# for name in list:
#     if name.startswith("S"):
#         print(f"Hello {name}!")



# n = int(input("Enter number: "))
# for i in range(1, 11):
#     print(f"{n} X {i} = {n*i}")


# n = int(input("Enter number: ")) 
# i = 1
# while i <=10:
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# n = int(input("Enter number: "))

# for i in range(2, n):
#     if n%i == 0:
#         print(f"{n} is not a prime number.")
#         break
# else:
#     print(f"{n} is a prime number.")
    





# n = int(input("Enter number: "))

# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1

# print(sum)

# n = int(input("Enter number: "))
# product = 1
# for i in range(1, n+1):
#     product *= i
# print(f"Factorial of {n} is: {product}")

   

# n = int(input("Enter number: "))
# for i in range(1, n+1):
#     print(i* "*" , end = " ")
#     print(" ")


# n = int(input("Enter number: "))

# for i in range(10, 0, -1):
#     print(f"{n} X {i} = {n*i}")



# def average():
#     n = int(input("Enter number of subjects: "))
#     total = 0
#     for i in range(n):
#         marks = int(input(f"Enter marks for subject {i+1}: "))
#         total += marks
#     avg = total / n
#     print(f"Average marks: {avg}")

# average()

# def greet(name):
#     print(f"hello! {name}")


# greet("SHUBHAM")

# def greet(name, ending):
#     print(f"Hello {name}{ending}")
#     return name

# a = greet("Shubham", " Kaushik")

# print(a)

# def sum(n):
#     if n == 1 :
#         return 1
#     return sum(n-1) + n

# print(sum(8))

# with open("file.txt", "r") as f:
#     line = f.readline()
#     while (line != ""):
#         print(line)
#         line = f.readline()

# with open("file.txt", "r") as f:
#     content = f.read()
#     print(content)
#     if "anything" in content:
#         print("Word Found in the file...")
#     else:
#         print("Not Found...")


# import random
# def game():
#     score = random.randint(1,100)

#     with open("file.txt") as f:
#         hiscore = f.read()
#         if hiscore != "":
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#         print(f"Your Score: {score}")

#     if score > hiscore:
#         with open("file.txt", "w") as f:
#             f.write(str(score))
#     return score

# game ()

# def table_generator(n):
#       table = ""
#       for i in range(1,11):
#             table += f"{n} X {i} = {n*i}\n"

#       with open(f"tables/table_{n}", "w") as f:
#           f.write(table)

# for i in range(2,21):
#       table_generator(i)

# word = ["Donkey", "Monkey", "Gawar"]

# with open("file.txt", "r") as f:
#     content = f.read()

#     for i in word:
#         content = content.replace(i, "#"* len(word))
#         with open("file.txt", "w") as f:
#             f.write(content)

# Create a function check_even_odd(num) that returns whether a number is even or odd.


# print("Hello World")


# name = input("Enter Name: ")
# marks = int(input("Enter Marks: "))
# mobile_no = int(input("Enter Mobile number: "))

# format = "The name of the student is {} he got {} marks and his mobile number is {}".format(name, marks, mobile_no)

# print(format)

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))

# function = input("Enter Function: -, +, / , % ?")

# def calc():
#     if function == "-":
#         print(f"Substraction of {a} and {b} is {a-b}")
#     elif function == "+":
#         print(f"Addition of {a} and {b} is {a+b}")
#     elif function == "/":
#         print(f"Division of {a} and {b} is {a/b}")
#     elif function == "*":
#         print(f"Multiplication of {a} and {b} is {a*b}")
#     else:
#         print("There is some error!!")


# print(calc)

# Write a program using functions to find greatest of three numbers. 

# def greatest(x,y,z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     elif z > y and z > x:
#         return z
# print(greatest(12, 23,123))


# a = 43
# b = 42
# sum = a+b
# print(sum)

# n = int(input("Enter number: "))

# remainder = n%2
# print(remainder)

# a = input("Enter something: ")
# print(type(a))

# a = 34
# b = 80

# print(a>b)

# num1 = int(input("Enter 1st no. : "))
# num2 = int(input("Enter 2nd no. : "))

# average = (num1+num2)/2

# print(average)

# n = int(input("Enter number: "))
# square = n*n
# square1 = n**2

# print(square ,square1)

# name = input("Enter name: ")
# print(f"Good Afternoon, {name}!")

# name = "Shubham"
# date = "31st December"
# print(f'''
# Dear {name}
#     You're selected!
#     {date}''')

# string = "hello  there"
# print(string.find("  "))
# print(string.replace("  ", " "))

# letter = "Dear Sir, \n\tThis Python Course is nice! \n\tThanks!"
# print(letter)

# fruits = []
# x = input("Enter fruit name:")
# fruits.append(x)
# x = input("Enter fruit name:")
# fruits.append(x)
# x = input("Enter fruit name:")
# fruits.append(x)
# x = input("Enter fruit name:")
# fruits.append(x)
# x = input("Enter fruit name:")
# fruits.append(x)
# x = input("Enter fruit name:")
# fruits.append(x)
# x = input("Enter fruit name:")
# fruits.append(x)

# print(fruits)

# marks = []

# x = int(input("Enter Marks:"))
# marks.append(x)
# x = int(input("Enter Marks:"))
# marks.append(x)
# x = int(input("Enter Marks:"))
# marks.append(x)
# x = int(input("Enter Marks:"))
# marks.append(x)
# x = int(input("Enter Marks:"))
# marks.append(x)
# x = int(input("Enter Marks:"))
# marks.append(x)

# marks.sort()
# print(marks)

# list = [12, 23, 3, 34]
# total_sum = sum(list)
# print(total_sum)

# a = (7, 0, 8, 0, 0, 9)
# print(a.count(0))

# dict = {
#     "a" : 1,
#     "b" : 2,
# }

# print(dict["a"])

# dict = {
#     "Savagat" : "Welcome",
#     "Kaha" : "Where",
#     "Thik hai" : "Okay",
# }

# word = input("Enter word: ")

# print(f"The meaning of {word} in English is : {dict[word]}")


# set = set()

# x = int(input("Enter number: "))
# set.add(x)
# x = int(input("Enter number: "))
# set.add(x)
# x = int(input("Enter number: "))
# set.add(x)
# x = int(input("Enter number: "))
# set.add(x)
# x = int(input("Enter number: "))
# set.add(x)
# x = int(input("Enter number: "))
# set.add(x)
# x = int(input("Enter number: "))
# set.add(x)
# x = int(input("Enter number: "))
# set.add(x)

# print(set)

# set = {18, "18"}
# print(set)

# set = set()
# set.add(20)
# set.add(20.0)
# set.add("20")
# print(set)

# s = {}
# print(type(s))

# dict = {}
# lang = input("enter your fav. lang: ")
# dict.update({"Rohan" : lang})
# lang = input("enter your fav. lang: ")
# dict.update({"Shubham" : lang})
# lang = input("enter your fav. lang: ")
# dict.update({"Harry" : lang})
# lang = input("enter your fav. lang: ")
# dict.update({"Carry" : lang})

# print(dict)

# a = int(input("enter number: "))
# b = int(input("enter number: "))
# c = int(input("enter number: "))
# d = int(input("enter number: "))

# if a > b and a > c and a > d:
#     greatest = a
# elif b > a and b > c and b > d:
#     greatest = b
# elif c > a and c > b and c > d:
#     greatest = c
# elif d > a and d > b and d > c:
#     greatest = d
# else:
#     print("Something went wrong...")

# print(f"The greatest of 4 number is {greatest}")

# phy = int(input("Enter Marks: "))
# chem = int(input("Enter Marks: "))
# maths = int(input("Enter Marks: "))

# total = ((phy + chem + maths)/300) * 100

# if total > 40 and phy >= 33 and chem >= 33 and maths >= 33:
#     print(f"Student has scored {total}% and he is pass!")
# else:
#     print("Student Failed")


# comment = "hey there make a lot of money"

# word1 = "make a lot of money"
# word2 = "subscribe this"
# word3 = "buy now"

# if word1 in comment or word2 in comment or word3 in comment:
#     print("Word found")
# else:
#     print("not found")

# username = input("enter username: ")

# if len(username) >= 10:
#     print("All set!")
# else:
#     print("Must be 10 letters!")

# list = ["Shubham", "Harry", "Rohit", "Arya"]
# name = input("Enter name: ")

# if name in list:
#     print("Yes, name is present!")
# else:
#     print("Not present!")

# post = "harry is a good harry. harry is haary"

# if "harry" in post:
#     print("Yes, Present in post")
# else:
#     print("Not present")

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     grade = "Excellent"
# elif marks >=80 and marks < 90:
#     grade = "A"
# elif marks >=70 and marks < 80:
#     grade = "B"
# elif marks >=60 and marks < 70:
#     grade = "C"
# elif marks >=50 and marks < 60:
#     grade = "D"
# elif marks < 50:
#     grade = "Fail"

# print(f"You entered marks : {marks} so your grade is {grade}")

# n = int(input("Enter number: "))

# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

# i = 1
# while i < 11:
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# l1 = ["Harry", "Shubham", "Sachin", "Rahul"]

# for names in l1:
#     if names.startswith("S"):
#         print(f"Hello, {names}")

# n = int(input("Enter number: "))

# for i in range(2,n):
#     if n%i!=0:
#         print(f"{n} is a prime number.")
#         break
#     else:
#         print(f"{n} is not a prime number.")

# first n natural numbers

# n = int(input("Enter number: "))

# i = 1
# sum = 0
# while i < n+1:
#     sum += i
#     i += 1

# print(sum)

# using for loop find the factorial of a given number

# n = int(input("Enter number: "))

# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print(fact)

# Using for loop print a reversed table of a number

# n = int(input("Enter number: "))

# for i in range(10, 0, -1):
#     print(f"{n} X {i} = {n*i}")

# '''
# *
# **
# ***
# '''

# for i in range(1, 4):
#     print("*" * i)

# n = int(input("enter number: "))

# for i in range(n, 0, -1):
#     print("*" * i)


# def greatest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     elif c > a and c > b:
#         return c

# print(greatest(7, 9, 12))

# def greatest(a, b, c):
#     return max(a, b, c)

# print(greatest(2, 3, 4))


# def converter(c):
#     return (c * (9/5))+ 32

# print(converter(1382481))


# print("Shubham ", end = " ",)

# Recursion for first n natural numbers

# n = int(input("enter number: "))
# def sum(n):
#     if n==1:
#         return 1
#     return n + sum(n-1)
# print(sum(n))


# convert inches to centimeters

# def inch_to_cm(inch):
#     return inch * 2.54

# print(inch_to_cm(12))

# Multiplication table of a given number

# def table(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")
    
# table(67)

