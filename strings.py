# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function.

name = input("Enter your name: ")
print(f"Good afternoon, {name}!")

# 2. Write a program to fill in a letter template given below with name and date. 
'''
        letter = ''  
        Dear <|Name|>, 
        You are selected! 
        <|Date|> 
        ''
'''

name = input("Enter name: ")
date = input("Enter date: ")
print(
    f'''Dear {name},
    Your are selected!
    {date}
'''
)

# 3. Write a program to detect double space in a string.

string = "Here I write anything  !"
print(string.find("  "))  # At index 21

# 4. Replace the double space from problem 3 with single spaces. 

string = "Here I write anything  !"
print(string.replace("  ", " "))

# 5. Write a program to format the following letter using escape sequence 
# characters. 
'''
    letter = Dear Teacher, this python course is nice. Thanks!
'''

letter = "Dear Teacher, \n\tThis python course is nice. \n\tThanks!"
print(letter)