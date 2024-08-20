"""
In short, a factorial is a function that multiplies a number by every number below it till 1. 
For example, the factorial of 3 represents the multiplication of numbers 3, 2, 1, 
i.e. 3! = 3 * 2 * 1 and is equal to 6.

"""

num =  int(input("Enter any number"))
if num<0:
    print(f"No Factorial fo the number{num}")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    fact = 1
    for i in range(1,num+1):
        fact*=i 
    print(f"The factorial for {i} is {fact}")
