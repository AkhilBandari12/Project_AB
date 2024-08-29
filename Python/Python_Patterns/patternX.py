



n = int(input("Enter any num"))


# for i in range(n):
#     for k in range(i):
#         print("A",end=" ")
#     for j in range(1):
#         print("*",end=" ")
#     for m in range(n-i):
#         print("B",end=" ")
#     for n in range(1):
#         print("*")



for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()














