# 1. Write a program to store seven fruits in a list entered by the user.

fruits = []
x = input("Enter 1st fruit name: ")
fruits.append(x)
x = input("Enter 2nd fruit name: ")
fruits.append(x)
x = input("Enter 3rd fruit name: ")
fruits.append(x)
x = input("Enter 4th fruit name: ")
fruits.append(x)
x = input("Enter 5th fruit name: ")
fruits.append(x)
x = input("Enter 6th fruit name: ")
fruits.append(x)
x = input("Enter 7th fruit name: ")
fruits.append(x)

print(fruits)


# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner.

marks = []
x = int(input("Enter Marks of 1st student: "))
marks.append(x)
x = int(input("Enter Marks of 2nd student: "))
marks.append(x)
x = int(input("Enter Marks of 3rd student: "))
marks.append(x)
x = int(input("Enter Marks of 4th student: "))
marks.append(x)
x = int(input("Enter Marks of 5th student: "))
marks.append(x)
x = int(input("Enter Marks of 6th student: "))
marks.append(x)

marks.sort()
print(marks)


# 3. Check that a tuple type cannot be changed in python. 

tuple = (1, 2, 3)
tuple[0] = 5       # TypeError will occur


# 4. Write a program to sum a list with 4 numbers.

list = [1, 3, 4, 6]
sum = sum(list)
print(sum)


# 5. Write a program to count the number of zeros in the following tuple: 
'''
    a = (7, 0, 8, 0, 0, 9)
'''

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))