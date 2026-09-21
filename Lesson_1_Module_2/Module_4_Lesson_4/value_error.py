try: 
    number = int(input("enter a number: "))
    print("The number you entered is:", number)
except ValueError as ex:
    print ("Exception", ex)
