"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

strs = ["flower","flow","flight"]

op = ""


l = len(strs[0])

for i in range(l):
    temp = ""
    for j in strs:
        if len(j)>=i:
            temp+=j
