"""
     *
    * *
   * * * 
  * * * *
 * * * * *
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

"""

num = int(input("Enter num of Rows "))

for i in range(num):
    for j in range(num-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()
for n in range(num):
    for l in range(n+1):
        print(" ",end="")
    for m in range(num-n-1):
        print("*",end=" ")
    print()


