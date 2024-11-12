"""


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


"""


l1 = [2,4,3]
l2 = [5,6,4]



a = int("".join([str(i) for i in l1[::-1]]))
b = int("".join([str(j) for j in l2[::-1]]))

res = a+b

print([int(k) for k in str(res)][::-1])
