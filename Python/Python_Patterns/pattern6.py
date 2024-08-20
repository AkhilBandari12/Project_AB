"""
11111
2222
333
44
5

"""


num = int(input("Enter num of Rows "))

for i in range(1,num+1):
    for j in range(num-i+1):
        print(i,end=" ")
    print()