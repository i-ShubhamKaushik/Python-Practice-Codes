# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

dictionary = {
    "kya" : "what",
    "kab" : "when",
    "acha" : "okay",
    "shabad" : "word"
}
word = input("Enter word whose meaning you want to know in english!: ")
if word in dictionary:
     print(f"The meaning of {word} in english is: {dictionary[word]}")
else:
     print(f"Sorry, {word} is not in dictionary")


# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).

set = set()
x = int(input("Enter number: " ))
set.add(x)
x = int(input("Enter number: " ))
set.add(x)
x = int(input("Enter number: " ))
set.add(x)
x = int(input("Enter number: " ))
set.add(x)
x = int(input("Enter number: " ))
set.add(x)
x = int(input("Enter number: " ))
set.add(x)
x = int(input("Enter number: " ))
set.add(x)
x = int(input("Enter number: " ))
set.add(x)

print(set)


# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

set = {18, "18"}
print(set)        # Yes, both are treated as seprate values!

# 4. What will be the length of following set s: 
'''
    s = set() 
    s.add(20) 
    s.add(20.0) 
    s.add('20') # length of s after these operations? 
'''

s = set()
s.add(20.0) 
s.add(20) 
s.add('20')
print(s)      # 20 and 20.0 are treated as equal. So, it will only display once


# 5. s = {} 
# What is the type of 's'?

s = {}
print(type(s))  # Dict class, Because empty sets are : set()


# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

dict = {}
name = input("Enter name: ")
lang = input("Enter favouite programming language: ")
dict.update({name: lang})
name = input("Enter name: ")
lang = input("Enter favouite programming language: ")
dict.update({name: lang})
name = input("Enter name: ")
lang = input("Enter favouite programming language: ")
dict.update({name: lang})
name = input("Enter name: ")
lang = input("Enter favouite programming language: ")
dict.update({name: lang})

print(dict)


# 7. If the names of 2 friends are same; what will happen to the program in problem 
# 6?

dict = {}
name = "Shubham"
lang = input(f"Enter favouite programming language of {name}: ")
dict.update({name: lang})
name = "Shubham"
lang = input(f"Enter favouite programming language of {name}: ")
dict.update({name: lang})
name = input("Enter name: ")
lang = input("Enter favouite programming language: ")
dict.update({name: lang})
name = input("Enter name: ")
lang = input("Enter favouite programming language: ")
dict.update({name: lang})

print(dict)                  # Secomd value will overwrite the 1st value


# 8. If languages of two friends are same; what will happen to the program in problem 
# 6?

dict = {}
name = input("Enter name: ")
lang = "Python"
dict.update({name: lang})
name = input("Enter name: ")
lang = "Python"
dict.update({name: lang})
name = input("Enter name: ")
lang = input("Enter favouite programming language: ")
dict.update({name: lang})
name = input("Enter name: ")
lang = input("Enter favouite programming language: ")
dict.update({name: lang})

print(dict)                    # Nothing will happen! They will be treated seprate!


# 9. Can you change the values inside a list which is contained in set S? 
'''
    s = {8, 7, 12, "Harry", [1,2]}
'''

print("Not Possible.!")