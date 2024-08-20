"""

This is a staircase of size : n = 4

   #
  ##
 ###
####

"""



def staircase(n):
    # Write your code here
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i+1):
            print("#",end="")
        print()


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)