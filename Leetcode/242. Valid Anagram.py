"""


Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.
 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


"""

s = "anagram"
t = "nagaram"

# s = "rat"
# t = "cart"

s_lis = sorted(list(s))
t_lis = sorted(list(t))

if s_lis == t_lis:
    print(s_lis)
    print(t_lis)
    print("True")
else:
    print("False")