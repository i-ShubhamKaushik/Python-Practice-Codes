# 1. Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")


# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
l = ["Vyuk", "Shubham", "Sachin", "Rahul"]

for name in l:
    if name.startswith("S"):
        print(f"Hello, {name}!")


# 3. Attempt problem 1 using while loop. 

n = int(input("Enter number: "))

i = 1
while i <= 10:
    print(f"{n} X {i} = {n*i}")
    i += 1


# 4. Write a program to find whether a given number is prime or not. 

num = int(input("Enter number: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a Prime number!")
        break
    else:
        print(f"{num} is a Prime number!")
        break


# 5. Write a program to find the sum of first n natural numbers using while loop. 

num = int(input("Enter number: "))
sum = 0

i = 1
while i <= num:
    sum += i
    i += 1
print(sum)


# 6. Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter number: "))

factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f"The factorial of {num} is : {factorial}")


# 7. Write a program to print the following star pattern. 

'''    
        * 
       *** 
      *****   for n = 3
'''

n = 3
for i in range(1, n+1):
     print(" " * (n - i), end="")
     print("*" * (2 * i - 1))


# 8. Write a program to print the following star pattern: 
'''     * 
        ** 
        ***      for n = 3
'''
n = 3
for i in range(1, n+1):
    print("*" * i)


# 9. Write a program to print the following star pattern. 
'''
        * * * 
        *   *   for n = 3 
        * * * 
'''

n = 3

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 10. Write a program to print multiplication table of n using for loops in reversed 
# order. 

n = int(input("Enter number: "))
for i in range(10, 0, -1):
    print(f"{n} X {i} = {n*i}")