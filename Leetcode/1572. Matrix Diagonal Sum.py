"""

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal 
that are not part of the primary diagonal.

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5

"""

# mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[5]]
l = len(mat)
op_sum = 0


for i in range(l):
    print(i)
    op_sum+= mat[i][i]+mat[i][l-i-1]

if l%2==1:
    print("PPPPPP")
    op_sum-=mat[l//2][l//2]
print(op_sum)