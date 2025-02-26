"""

You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the diagonals of nums.
In case, no prime is present on any of the diagonals, return 0.


"""


nums = [[1,2,3],[5,6,7],[9,10,11]]

# print(len(nums[1]))
frst_diag = 0 
sec_diag = 0
op = []

for i in range(len(nums)):
    # print(i,"Th ROW")
    # print(len(nums[i]))
    for j in range(len(nums[i])):
        if i==j or i+j==len(nums)-1:
            # print(nums[i][j],"11111")
            # frst_diag+=nums[i][j]
            n = nums[i][j]
            c = 0
            for k in range(1,n+1):
                if n%k==0:
                    c+=1
            if c==2:
                op.append(n)
            
        # elif i+j==len(nums)-1:
        #     # print(i,j,len(nums))
        #     # print(nums[i][j],"2222222")
        #     # sec_diag+=nums[i][j]

# print(frst_diag,sec_diag)
print(max(op))