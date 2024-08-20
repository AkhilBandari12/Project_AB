"""
1
22
333
4444
55555

"""

num = int(input("Enter num of Rows "))

for i in range(1,num+1):
    for j in range(i):
        print(i,end=" ")
    print()