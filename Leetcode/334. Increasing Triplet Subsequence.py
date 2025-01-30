"""


Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.



"""


# nums = [5,4,3,2,1]
# nums = [1,2,3,4,5]
# nums = [2,1,5,0,4,6]
# nums = [20,100,10,12,5,13]
nums = [1,2,1,3]

res = False
for i in range(len(nums)-2+1):
    print(i,"loop")
    if i == len(nums)-2:
        # print("1st IF")
        if nums[i-2]<nums[i-1]<nums[0]:
            res = True
    elif i == len(nums)-1:
        print("2st IF")

        if nums[i-1]<nums[0]<nums[1]:
            res = True
    else:        
        print("ELSE IF")

        if nums[i]<nums[i+1]<nums[i+2]:
            res = True
print(res)
