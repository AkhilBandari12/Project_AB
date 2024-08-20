"""
A perfect square is a number, from a given number system, that can be expressed as the square of a number from the same number system.
 Examples of Numbers that are Perfect Squares. 25 is a perfect square. 25 is a natural number, and since there is another natural number 5, 
 such that 52 = 25, 25 is a perfect square.

"""

import math

n = int(input("Enter any number"))  
m = int(math.sqrt(n))
if m*m == n:
    print(f"{n} is perfect square")
else:
    print(f"{n} is not a perfect square")
