"""

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


"""


# digits = [1,2,3]
# digits = [4,3,2,1]
digits = [9]

s = [""+str(i) for i in digits]
m  = int("".join(s))+1
o = (list(str(m)))
op_ls =[]

for k in o:
    op_ls.append(int(k))

print(op_ls)