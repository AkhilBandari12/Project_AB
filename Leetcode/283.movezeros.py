"""


Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


"""

nums = [0,1,0,3,12]

p = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[p]=nums[i]
        p+=1
print(nums)

for k in range(p,len(nums)):
    nums[k]=0
print(nums)

