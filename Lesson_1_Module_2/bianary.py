n = int(input("Enter a number: "))
b = ""

while n > 0:
    while n > 0:
        b = str(n % 2) + b
        n = n // 2

print("Binary:", b)