try:
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")
except ValueError:
    print("Value Error: Please enter a whole number")