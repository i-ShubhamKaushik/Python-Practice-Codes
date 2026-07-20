# ===========================
# map() Practice Questions
# ===========================

# Q1. Given:

numbers = [2, 4, 6, 8, 10]

# Use map() with a lambda function to double every number.

square = lambda x : x*2
print(list(map(square, numbers)))



# Q2. Given:

names = ["rahul", "shubham", "aman", "riya"]

# Use map() with a lambda function to capitalize each name.

capitalize = lambda name: name.capitalize()
print(list(map(capitalize, names)))



# Q3. Given:

numbers = [10, 20, 30, 40]

# Use map() with a lambda function to convert every integer into a string.

convert = lambda number: str(number)
print(list(map(convert, numbers)))



# Q4. Given:

words = ["python", "java", "javascript", "c"]

# Use map() with a lambda function to find the length of every word.

length = lambda word: len(word)
print(list(map(length, words)))


# Q5. Given:

prices = [100, 250, 500, 800]

# Use map() with a lambda function to add 18% GST to every price.

gst = lambda price: price*1.18
print(list(map(gst, prices)))