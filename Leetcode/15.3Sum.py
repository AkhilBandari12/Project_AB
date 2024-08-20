nums = [-1,0,1,2,-1,-4]
op_list = []
res = []
l = len(nums)
# for i in range(l):
#     for j in range(i,l):
#         for k in range(i,l):
#             temp = nums[i]+nums[j]+nums[k]
#             if temp ==0:
#                 op_list.append([nums[i],nums[j],nums[k]])
# print(op_list)
            

for i in range(l):
    for j in range(l):
        for k in range(l):
            
            if i<l-2 and j<l-2 and k<l-2:
                temp = nums[i]+nums[j]+nums[k]
                if temp ==0:
                    op_list.append([nums[i],nums[j],nums[k]])

for i in op_list:

    if i not in res:
        res.append(i)

print(res)



