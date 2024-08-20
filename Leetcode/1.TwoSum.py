"""



Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]



"""

nums = [2,7,11,15]
target = 9

# nums = [3,2,4]
# target = 6

# nums = [3,2,3]
# target = 6


oplis  = []
pointer = 0

for i in range(len(nums)):
    for k in range(i+1,len(nums)):
        if nums[i]+nums[k]==target:
            oplis.append([i,k])

print(oplis)



# while pointer<=len(nums)-2:
#     if nums[pointer]+nums[pointer+1]==target:
#         # oplis.append([pointer,pointer+1])
#         oplis.append(pointer)
#         oplis.append(pointer+1)
#     pointer+=1
# print(oplis)

