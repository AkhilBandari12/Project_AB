"""

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""


nums = [0,0,1,1,1,2,2,3,3,4]
op_ls = []

n = sorted(nums)
c = 0
for i in nums:
    if i not in op_ls:
        op_ls.append(i)
    else:
        c+= 1
print(op_ls)
print(len(op_ls))

for k in range(c):
    op_ls.append("_")
print(op_ls)
print(len(op_ls))
