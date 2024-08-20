"""
0 1 1 2 3 5 8 13 .........

"""

######__________Given Range________####
num = int(input("Enter the range number "))
a=0
b=1
c = a

while a < num:
    print(c)
    a,b = b,c
    c=a+b


