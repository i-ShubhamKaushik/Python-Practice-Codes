# ===========================
# reduce() Practice Questions
# ===========================

from functools import reduce

# Q1. Given:
# from functools import reduce
#
numbers = [5, 10, 15, 20]
#
# Use reduce() with a lambda function to find the sum of all numbers.

add = lambda a,b: a + b
print(reduce(add, numbers))



# Q2. Given:
# from functools import reduce
#
numbers = [2, 3, 4, 5]
#
# Use reduce() with a lambda function to find the product of all numbers.

product = lambda a,b: a*b
print(reduce(product, numbers))



# Q3. Given:
# from functools import reduce
#
numbers = [15, 40, 8, 90, 32]
#
# Use reduce() with a lambda function to find the largest number.

largest = lambda a,b: a if a > b else b
print(reduce(largest, numbers))



# Q4. Given:
# from functools import reduce
#
words = ["Python", "is", "fun"]
#
# Use reduce() with a lambda function to join all words into a single sentence separated by spaces.

join = lambda a,b: a+ " " + b
print(reduce(join, words))




# Q5. Given:
# from functools import reduce
#
numbers = [100, 20, 10]
#
# Use reduce() with a lambda function to subtract the numbers from left to right.
# (Example: ((100 - 20) - 10))

subtract = lambda a,b: a-b
print(reduce(subtract, numbers))