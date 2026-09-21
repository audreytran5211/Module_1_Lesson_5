try: 
    num1, num2 = eval(input("enter two numbers, sperated by a coma :"))
    result = num1 / num2
    print("The result of the divison is:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")

except SyntaxError: 
    print("Coma is missing, please enter two numbers separated by a coma.")

except:
    print("wrong input")

else:
    print("no exceptions")

finally: 
    print("this will execute NO matter what.")