import math
# math is a python library that uses math funcs
def circumference():
    radius = float(input("enter the radius of the circle: "))
    answer = 2 * math.pi * radius
    # using the math.pi function, it helps plug in 3.14 for pi to solve for circumfrerence 
    print("the circumference is:" , answer)

circumference()
