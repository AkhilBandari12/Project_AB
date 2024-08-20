"""
amicable numbers, in mathematics, a pair of integers in which each is the sum of the divisors of the other.
The first pair of amicable (“friendly”) numbers, 220 and 284, was discovered by the ancient Greeks

Note: 220 and 284 are examples of amicable numbers.
The factors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110, which sum to 284,
while the factors of 284 are 1, 2, 4, 71, and 142, which sum to 220

"""
###******Amicable Number**********########

num1 = int(input("enter any number"))
num2 = int(input("enter any number"))
sum1 = 0
sum2 = 0 
for i in range(1,num1):
    if num1%i==0:
        sum1+=i
for j in range(1,num2):
    if num2%j==0:
        sum2+=j
print(f'sum1{sum1},sum2:{sum2}')
if sum1==num2 and sum2==num1:
    print("The numbers are Amicable")
else:
    print("Not Amicable")


######**********Amicable Number in A Range************##########

lower_range = int(input("Enter the lower limit"))
upper_range = int(input("enter the upper limit"))
for i in range(lower_range,upper_range+1):
    num1 = i 
    sum1=0
    sum2=0
    for k in range(1,num1):
        if num1%k==0:
            sum1+=k
    num2 = sum1
    for j in range(1,sum1):
        if num2%j==0:
            sum2+=j
    if sum1==num2 and sum2==num1 and num1!=num2:
        print(num1,num2)
    