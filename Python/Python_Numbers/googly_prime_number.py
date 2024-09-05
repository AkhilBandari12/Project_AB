"""


N = 43
4+3 = 7 

7 is Prime number so  43 is a googly prime number 


"""


n = input("enter any number")
m = 0 
for i in n:
    m+= int(i)
count = 0
for i in range(1,m+1):
    if m%i==0:
        count+=1
if count==2:
    print(f"{n} is a Googly Prime number")
else:
    print(f"{n} is not a Googly prime number")

