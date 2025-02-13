"""
Find first non-repeating character of given string
Last Updated : 25 Oct, 2024
Given a string s of lowercase English letters, the task is to find the first non-repeating character. If there is no such character, return ‘$’.

Examples: 

Input: s = “geeksforgeeks”
Output: 'f'
Explanation: 'f' is the first character in the string which does not repeat.


Input: s = “racecar”
Output: 'e'
Explanation: 'e' is the only character in the string which does not repeat.


Input: “aabbccc”
Output: '$'
Explanation: All the characters in the given string are repeating.

"""


# s = "geeksforgeeks"
s = "racecar"
# s = "aabbccc"

for i in s:
    if s.count(i)>1:
        continue
    else:
        print(i)
        break
print("$$$$$$$$$")

