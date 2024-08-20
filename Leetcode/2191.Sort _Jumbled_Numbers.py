"""

Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
Output: [338,38,991]
Explanation: 
Map the number 991 as follows:
1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
Therefore, the mapped value of 991 is 669.
338 maps to 007, or 7 after removing the leading zeros.
38 maps to 07, which is also 7 after removing leading zeros.
Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
Thus, the sorted array is [338,38,991].


"""

# mapping = [8,9,4,0,2,1,3,5,7,6]
# nums = [991,338,38]

mapping = [5,6,8,7,4,0,3,1,9,2]
nums = [7686,97012948,84234023,2212638,99]
map_nums = []
op_ls = []
for i in nums:
    temp = str(i)
    num_temp = ""
    for k in temp:
        p = mapping[int(k)]
        num_temp+=str(p)
    map_nums.append((num_temp))
map_nums = sorted(map_nums)
print((map_nums))

for x in map_nums:
    st = ''
    for k in x:
        # print(k)
        y = mapping.index(int(k))
        # print(y)
        # val = str(mapping[y])
        st+=str(y)
    op_ls.append(int(st))
print(op_ls)
