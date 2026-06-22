# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c>= b:
        return c
    
print(greatest(3,4,1))


# 2. Write a python program using function to convert Celsius to Fahrenheit.

def convertor(c):
    return (c*1.8) + 32

print(convertor(53))


# 3. How do you prevent a python print() function to print a new line at the end.

print("Hello", end = " ")
print("World")


# 4. Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter how many natural numbers you want to add: "))

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

print(sum(n))


# 5. Write a python function to print first n lines of the following pattern: 
'''
        *** 
        **               
        *     - for n = 3
'''

n = 3

def func(n):
    for i in range(n, 0, -1):
        print("*" * i)

func(n)


# 6. Write a python function which converts inches to cms.

def inches_to_cm(n):
    print(n* 2.54)

inches_to_cm(12)


# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time.

def rem(l, word):
    n = []

    for item in l:
        if item.strip() != word:
            n.append(item.strip())
    return n

l = ["Harry", "Rohan", "Shubham", "an"]

print(rem(l, "an"))


# 8. Write a python function to print multiplication table of a given number. 

n = int(input("Enter number: "))

def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

table(n)