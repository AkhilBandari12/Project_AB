"""

Sum of Digits

Enter a number:157
The total sum of digits is: 13

"""


#########________Method 1_____________###############

num = input("enter any num")
sum = 0
for i in num:
    sum+=int(i)
print(sum)


############________Method 2 ____________###########

num = int(input("Enter any num"))
sum = 0

while(num>0):
    temp = num%10
    sum+=temp
    num = num//10

print(sum)