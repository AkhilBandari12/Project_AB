"""


Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


"""


a = "100"
b = "1"

s = a[::-1]
print(s)
val = 0
for i in range(len(a)):
    temp = int(s[i])
    if temp == 1:
        val+= 2**i
    
print(val)
print(bin(val)[2::])
print(type(bin(val)))