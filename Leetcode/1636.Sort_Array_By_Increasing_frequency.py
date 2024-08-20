"""

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.


"""

nums = [1,1,2,2,2,3]

set_ls = list(set(nums))
print(set_ls)
op_ls = []
for i in set_ls:
    c = nums.count(i)
    op_ls.append(c)

# res = sorted({k:v for k,v in zip(set_ls,op_ls)})
res = {k:v for k,v in zip(set_ls,op_ls)}
print(res)
val = sorted([v for v in res.values()])

print(val)







# op_ls =[]
# cou = nums.count(nums[0])
# for i in set_ls:
#     temp = nums.count(i)
#     if temp <= cou:
#         op_ls[0:1] = i 
#     else:
#         op_ls[1:2] = i

# print(op_ls)
