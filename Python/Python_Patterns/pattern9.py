"""
   1
  121
 12321 
1234321
 12321
  121
   1


"""


num = int(input("Enter num of Rows "))

for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for q in range(i-1,0,-1):
        print(q,end=" ")
    print()
for n in range(1,num+1):
    for l in range(n):
        print(" ",end=" ")
    for m in range(1,num-n+1):
        print(m,end=" " )
    for r in range(num-n-1,0,-1):
        print(r,end=" ")
    print()
