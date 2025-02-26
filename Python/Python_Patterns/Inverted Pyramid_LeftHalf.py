"""

* * * * *    |    1 2 3 4 5    |    A B C D E
  * * * *    |      1 2 3 4    |      A B C D
    * * *    |        1 2 3    |        A B C
      * *    |          1 2    |          A B
        *    |            1    |            A

"""


n = int(input("Enter any number"))


for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()


for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(1,n-i+1):
        print(k,end=" ")
    print()



for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print(chr(65+k),end=" ")
    print()