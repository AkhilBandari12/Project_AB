"""

Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.


Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.


"""


n = 4
c = 0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        # print(c)

if c==3:
    print(True)
else:
    print(False)
