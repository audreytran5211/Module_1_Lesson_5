def add(P, Q):
    # def is always added before a function
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

print("Please select an operation:")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

choice = input("enter a choice (a/b/c/d): ")
#choice is the user input for the operation
num_1 = int(input("enter first number: "))
num_2 = int(input("enter second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))

else:
    print("invalid input")
