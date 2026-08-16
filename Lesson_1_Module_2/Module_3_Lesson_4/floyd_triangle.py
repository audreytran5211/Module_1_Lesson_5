rows = int(input("enter the total number of rows for the floyd triangle: "))
num = 1
print("floyd triangle pattern of numbers:")
for i in range(0,rows):
    for j in range(0, i + 1):
        print(num, end=" ")
        num += 1
    print()