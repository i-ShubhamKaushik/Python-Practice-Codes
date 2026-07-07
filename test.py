try:
    file = input("\nEnter file name: ")
    with open(f"{file}", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\nThis file doesn't exist\n")