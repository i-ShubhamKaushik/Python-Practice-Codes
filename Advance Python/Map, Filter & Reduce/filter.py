# ===========================
# filter() Practice Questions
# ===========================

# Q1. Given:

numbers = [12, 7, 25, 18, 9, 40]

# Use filter() with a lambda function to keep only even numbers.

def even(n):
    if n%2==0:
        return True
    return False

print(list(filter(even, numbers)))




# Q2. Given:

numbers = [-10, 5, 0, 12, -3, 20]

# Use filter() with a lambda function to keep only positive numbers.

def positive(n):
    if n>0:
        return True
    return False

print(list(filter(positive, numbers)))


# Q3. Given:

names = ["Aman", "Om", "Shubham", "Riya", "Rahul"]

# Use filter() with a lambda function to keep only names having more than 4 letters.

length = lambda name: len(name) > 4
print(list(filter(length, names)))



# Q4. Given:

ages = [12, 18, 21, 15, 30, 17]

# Use filter() with a lambda function to keep only people eligible to vote (age >= 18).

eligible = lambda age: age>=18
print(list(filter(eligible, ages)))



# Q5. Given:

words = ["apple", "", "banana", "", "grape", ""]

# Use filter() with a lambda function to remove all empty strings.

empty = lambda word: word!=""
print(list(filter(empty, words)))
print(words)