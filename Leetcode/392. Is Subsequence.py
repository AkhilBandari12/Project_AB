"""


Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


"""


# s = "axc"
# t = "ahbgdc"

s ="aaaaaa"
t ="bbaaaa"

s_pointer = 0
t_pointer = 0

while s_pointer<len(s) and t_pointer<len(t):
    if s[s_pointer]==t[t_pointer]:
        s_pointer +=1
    t_pointer +=1

if s_pointer==len(s):
    print("True")
else:
    print("False")

# sp = tp = 0

# while sp < len(s) and tp < len(t):
#     if s[sp] == t[tp]:
#         sp += 1
#     tp += 1

# print( "drftghkjl;")