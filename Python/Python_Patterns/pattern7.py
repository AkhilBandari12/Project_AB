"""
1
23
456
78910

"""


num = int(input("Enter num of Rows "))

count=1
for i in range(1,num+1):
    for j in range(i):
        print(count,end=" ")
        count+=1
    print()
