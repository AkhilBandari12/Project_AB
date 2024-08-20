"""

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


"""
import math
# nums1 = [1,3]
# nums2 = [2]
# nums1 = [1,2]
# nums2 = [3,4]

# nums1 = [1,3]
# nums2 = [2,7]

# nums1 = []
# nums2 = [1,2,3,4,5]

nums1 = []
nums2 = [1]


op_lis = sorted(nums1+nums2)
l = len(op_lis)
sum = 0 
if op_lis:
    if l%2== 0:
        k = int(l/2)
        print(k)
        j = op_lis[k-1] + op_lis[k]
        r =j/2
        print(r)
    elif l%2==1 and l>1:
        # print("hhhhhh")
        r = math.floor(l/2)
        # print(r)
        print(float(op_lis[r]))
    elif l==1:
        print(float(op_lis[0]))
else:
    print()



# if l%2==0:
#     pass

# else:
#     pass

