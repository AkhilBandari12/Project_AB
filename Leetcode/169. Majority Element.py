"""


Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2




"""


# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]

set_list = list(set(nums))
cou = 0
element = nums[0]

for i in set_list:
    if nums.count(i)>cou:
        cou = nums.count(i)
        element = i
print(element)