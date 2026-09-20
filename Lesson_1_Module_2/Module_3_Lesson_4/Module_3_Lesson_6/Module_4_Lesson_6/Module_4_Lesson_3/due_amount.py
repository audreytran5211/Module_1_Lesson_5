def calculate_change(total, paid):
    change = paid - total
    return change

total = float(input("Enter the total bill: $"))
paid = float(input("Enter the amount paid: $"))

change = calculate_change(total, paid)

print("The shopkeeper should return: $", change)