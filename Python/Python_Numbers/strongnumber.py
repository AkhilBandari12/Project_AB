"""
A Strong number is a special number whose sum of the all digit factorial should be equal to the number itself.

For Exampler : 145 find the factorial 1! = 1, 4! = 24, and 5! = 120.
"""

#########________Strong Number _____________#########

temp =(input("Enter any number"))
num = int(temp)
sum = 0
def fact(anynum):
    res =1
    if anynum==0 or anynum==1:
        return 1
    else:
        for k in range(1,anynum+1):
            res*=k
    return  res

for i in temp:
    sum+= fact(int(i))
    print(sum)
if num == sum:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is not a Strong Number")


