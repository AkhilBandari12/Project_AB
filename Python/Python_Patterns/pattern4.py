"""
*****
 ****
  ***
   **
    *
"""

num = int(input("enter num of rows"))


for i in range(num):
    for j in range(i):
        print(" ",end="")
    for k in range(num-i):
        print("*",end="")
    print()