"""

* * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
  * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
    * * * * *       |       1 2 3 4 5       |       A B C D E
      * * *         |         1 2 3         |         A B C
        *           |           1           |           A


"""



n = int(input("Enter any number"))


for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    for k in range(1,n-i):
        print("*", end=" ")
    
    print()
