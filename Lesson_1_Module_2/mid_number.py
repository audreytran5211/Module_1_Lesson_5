numb = int(input("enter a number: "))
t = numb
numlen = 0
while t > 0:
    numlen = numlen+1
    t = int(t/10)

if numlen>=4:
    numlen = int(numlen/2)
    check = 0
    while numb>0:
        rem = numb%10
        if check == numlen:
            mid = rem
        elif check == (numlen-1):
            mid2 = rem
        numb = int(numb/10)
        check = check + 1
    print("the middle number is:", mid2, mid)
    product = mid*mid2
    print("the product of the middle numbers is:", product)
else:
    print("the number is less than 4 digits, so there is no middle number") 