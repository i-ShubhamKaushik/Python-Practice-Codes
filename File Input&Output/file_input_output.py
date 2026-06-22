# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

with open("file Input&Output/poem.txt", "r") as f:
    content = f.read()
    if "twinkle" in content.lower():
        print("Word found..!")
    else:
        print("Not found..!")


# 2. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.

def tables(n):   
    with open(f"File Input&Output/tables/table_of_{n}", "w") as f:
        for i in range(1,11):
            f.write(f"{n} X {i} = {n*i}\n")
            
for i in range(2,21):
    tables(i)


# 3. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  

with open("File Input&Output/donkey.txt", "r") as f:
    content = f.read()
    word = "donkey"
    if word in content:
        content = content.replace(word, "#"*len(word))
        with open("donkey.txt", "w") as f:
            f.write(content)


# 4. Repeat program 4 for a list of such words to be censored. 

words = ["donkey", "monkey", "rabbit", "snake"]

with open("File Input&Output/censored.txt", "r") as f:
    content = f.read()

    for word in words:
        content = content.replace(word, "#" * len(word))

        with open("File Input&Output/censored.txt", "w") as f:
            f.write(content)


# 5. Write a program to mine a log file and find out whether it contains ‘python’.

word = "python"
with open("File Input&Output/log.txt", "r") as f:
    content = f.read()
    if word in content.lower():
        print(f"Yes, The log file contains '{word}' in it.")
    else:
        print(f"No, The log file doesn't contains '{word}' in it.")


# 6. Write a program to make a copy of a text file “this.txt”

with open("File Input&Output/this.txt", "r") as f:
    content = f.read()
    with open("File Input&Output/copy.txt", "w") as f:
        f.write(content)


# 7. Write a program to find out whether a file is identical & matches the content of 
# another file.

with open ("File Input&Output/this.txt", "r") as f:
    content1 = f.read()
    with open ("File Input&Output/copy.txt", "r") as f:
        content2 = f.read()

    if content1 == content2:
        print("Yes, both files are identical..")
    else:
        print("No, files are not identical")


# 8. Write a program to wipe out the content of a file using python. 

with open("File Input&Output/wiped.txt", "w") as f:
    f.write("")


# 9. Write a python program to rename a file to “renamed_by_python.txt".

import os

if os.path.exists("File Input&Output/rename_this.txt"):
    os.rename("File Input&Output/rename_this.txt", "File Input&Output/renamed_by_python.txt")
    print("File renamed successfully..!")
else:
    print("File doesn't exist..!")