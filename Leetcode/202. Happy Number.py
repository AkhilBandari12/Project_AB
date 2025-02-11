"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false

"""
# n=19
# n =2
n=7

st_n = str(n)
# l = len(st_n)
c = 0    

if n<10:
    if n==1:
        print("happy Number")
    else:
        print("Not Happy Number")
else:
    while len(st_n)>1:    
        temp = 0
        for k in st_n:
            temp+=int(k)**2
            # print(temp)
        st_n = str(temp)
    if temp==1:
        print("happy Number")
    else:
        print("Not Happy Number")


# else:
#     if n==1:
#         print(True)

