try:
    age = int(input("Enter your age: "))
    print(f"your age is {age}")

except ValueError:
    print("Value Error: Age should be an integer")

finally:
    print("Final Statement")