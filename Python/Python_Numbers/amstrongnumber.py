"""
Armstrong number is a number that is equal to the sum of cubes of its digits.
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

Let's try to understand why 153 is an Armstrong number.
153 = (1*1*1)+(5*5*5)+(3*3*3)  

"""

# ########__________Amstrong Number__________########

temp = input("Enter any number : ")
power = len(temp)
num1 = int(temp)
num2 = 0
for i in temp:
    s = int(i)**power
    num2+= s
if num1==num2:
    print(f"{num1} is an Amstrong Number")
else:
    print(f"{num1} is not an Amstrong Number")

########______Amstrong Number in a Range___________#####

lower_limit = int(input("Enter any number"))
upper_limit = int(input("Enter any number"))

for i in range (lower_limit,upper_limit+1):
    temp = str(i)
    power = len(temp)
    val = 0
    for j in temp:
        s = int(j)**power
        val+= s
    if i == val:
        print(i, end=",")
print()




