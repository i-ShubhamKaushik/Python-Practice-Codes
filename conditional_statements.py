# 1. Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
d = int(input("Enter number: "))

if a >= b and a >= c and a >= d:
    greatest = a
elif b >= a and b >= c and b >= d:
    greatest = b
elif c >= a and c >= b and c >= d:
    greatest = c
elif d >= a and d >= b and d >= c:
    greatest = d

print(greatest)

# A better and easy way of doing it.
print(max(a,b,c,d))


# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

phy = int(input("Enters marks of physics: "))
chem = int(input("Enters marks of chemistry: "))
math = int(input("Enters marks of maths: "))

total = (phy + chem + math) / 3

if (
    total >=40 and
    phy >= 33 and
    chem >= 33 and
    math >= 33
):
    print("You are pass..!")
else:
    print("You are fail..!")


# 3. A spam comment is defined as a text containing following keywords: 
'''
    “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
    Write a program to detect these spams. 
'''

comment = input("Enter a comment: ").lower()

spam_words = [
    "make a lot of money",
    "buy now",
    "subscribe this",
    "click this"
]

is_spam = False

for word in spam_words:
    if word in comment:
        is_spam = True
        break

if is_spam:
    print("Spam detected...")
else:
    print("Not spam...")


# 4. Write a program to find whether a given username contains less than 10 
# characters or not

username = input("Enter username: ")
if len(username) >= 10:
    print("All set..!")
else:
    print("Length of username should be 10 atleast!")


# 5. Write a program which finds out whether a given name is present in a list or not. 

names = ["Shubham", "Rohit", "Carry", "Ram"]
if "Shubham" in names:
    print("Name found..!")
else:
    print("Not found..!")


# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
'''
    90 – 100 => Ex 
    80 – 90 => A 
    70 – 80 => B 
    60 – 70  =>C 
    50 – 60 => D 
    <50  => F
'''

marks = int(input("Enter marks: "))

if marks >= 90 and marks <=100:
    grade = "Excellent"
elif marks >= 80 and marks <90:
    grade = "A"
elif marks >= 70 and marks <80:
    grade = "B"
elif marks >= 60 and marks <70:
    grade = "C"
elif marks >= 50 and marks <60:
    grade = "D"
else:
    grade = "Fail"

print(grade)


# 7. Write a program to find out whether a given post is talking about “Vyuk” or not.

post = "Vyuk is a popular indian anime content creator!"

if "vyuk" in post.lower():
    print("Yes, Post is talking about Vyuk")
else:
    print("No, Post is not about vyuk")