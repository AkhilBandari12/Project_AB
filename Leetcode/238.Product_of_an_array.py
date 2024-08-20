"""

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

# nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
nums =[0,0]
op_ls = []
for i in range(len(nums)):
    prod = 1
    for k in range(len(nums)):
        if i != k:
            prod*=nums[k]
    op_ls.append(prod)


print(op_ls)
                






















# n = len(nums)
# result = [1] * n
# print(result)
# prefix_product = 1
# for i in range(n):
#     result[i] = prefix_product
#     prefix_product *= nums[i]
# suffix_product = 1
# for i in range(n-1, -1, -1):
#     result[i] *= suffix_product
#     suffix_product *= nums[i]
        
        

