"""

    1
   212
  32123
 4321234
543212345
 4321234
  32123
   212
    1 
"""
n = int(input("Enter any Number"))
for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for l in range(2,i+1):
        print(l,end=" ")
    print()

for p in range(1,n+1):
    for q in range(p+1):
        print(" ",end=" ")
    for r in range(n-p,0,-1):
        print(r,end=" ")
    for s in range(2,n-p+1):
        print(s,end=" ")
    print()