""""

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and
with the smallest space complexity possible.


Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), 
while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


"""
nums = [5,2,3,1]
pointer = 0 

ls =[]

for i in nums:
    if ls:
        print("****")
        for k in range(len(nums)):
            print("secondloop")
            print(i,nums[k])
            if i >nums[k]:
                print("condition")
                ls.append(i)
            else:
                ls[0] = i

    else:
         ls.append(i)


print(ls)





















































# from random import randint
# from typing import List

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def quick_sort(left, right):
#             if left >= right:
#                 return
#             pivot = nums[randint(left, right)]
#             less_than_pointer, greater_than_pointer, current = left - 1, right + 1, left
#             while current < greater_than_pointer:
#                 if nums[current] < pivot:
#                     less_than_pointer += 1
#                     nums[less_than_pointer], nums[current] = nums[current], nums[less_than_pointer]
#                     current += 1
#                 elif nums[current] > pivot:
#                     greater_than_pointer -= 1
#                     nums[greater_than_pointer], nums[current] = nums[current], nums[greater_than_pointer]
#                 else:
#                     current += 1
#             quick_sort(left, less_than_pointer)
#             quick_sort(greater_than_pointer, right)
#         quick_sort(0, len(nums) - 1)
#         return nums


