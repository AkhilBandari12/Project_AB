"""
A palindrome is a number (such as 16461) that remains the same when its digits are reversed.

"""

######_______Inbuilt Method________#######3

n = (input("Enter any number "))
res = ''.join(list(reversed(n)))
if n == res:
    print(f"{n} is a pallendrome")
else:
    print(f"{n} is not a pallendrome")


#######_________________Reverse Of a Num also work like below___________###########

#########___________Mathamatical_____#######

n = int(input("Enter any num"))
m = n
res =0
while n>0:
    remainder = n%10
    res=res*10+remainder
    n=n//10
if m==res:
    print("Pallendrome")
else:
    print("not a pallendrome number")

