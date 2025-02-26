"""

* * * * * 
*       * 
*       * 
*       * 
* * * * * 

"""



n = int(input("Enter Any Number"))



for i in range(1,n+1):
    for k in range(1,n+1):
        if (i==1 or k == 1 or i ==n or k==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()