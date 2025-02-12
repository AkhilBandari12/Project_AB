"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
 Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


"""



dict={
'2': 'abc',
'3': 'def',
'4': 'ghi',
'5': 'jkl',
'6': 'mno',
'7': 'pqrs',
'8': 'tuv',
'9': 'wxyz',}

# print(dict['2'])

ls =[]
op = []
digits = "234"
# digits = ""
# digits = "2"



for i in digits:
    # print(dict[i])
    ls.append(list(dict[i]))
# print(len(ls))

print(ls)
kp = len(ls)
if kp>1:
    for j in range(kp):
        if j < (kp-1):
            for k in ls[j]:
                for l in ls[j+1]:
                    op.append(str(k+l))
# elif kp ==0:
#     print("[]")
elif kp ==1:
    op = list(ls[0])

print(op)






