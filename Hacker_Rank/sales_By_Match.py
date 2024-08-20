"""


There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example


There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers, , the colors of the socks in the pile.

Constraints

 where 
Sample Input

STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
Sample Output

3


"""

import math



ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

s = list(set(ar))
# print(s)
op_count = 0
for i in s:
    # print(i)
    cou = ar.count(i)
    if cou >=2:
        # print(cou)
        temp = (cou//2)
        # print(temp)
        op_count+=temp
print(op_count)