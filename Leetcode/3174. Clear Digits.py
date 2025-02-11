"""

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

 

Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".





"""

s = "cb34"
S = list(s)
# op = ""
l = []

for i in S:
    print(i)
    if i.isalpha():
        # print(True)
        l.append(i)
        # print(l)
    elif i.isdigit():
        # print("---digit---")
        l.pop()
        # print(l)

print("".join(l))
        

# for k in l:
#     print(k)
#     s = s[:k-1] + s[k:]
#     print(s)
#     s = s[:k]+s[k+1:]
#     print(s)
# print(s)

# for i in range(len(s)):
#     print(i)
#     if i<len(s)-1:
#         st = s[i].isalpha()
#         num = s[i+1].isdigit()

#     if st is True and num is False:
#         op+=s[i]

# print(op)

