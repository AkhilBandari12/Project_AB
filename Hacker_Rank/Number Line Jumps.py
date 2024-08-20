"""


You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.


"""


x1 = 0 
v1 = 3 

x2 = 4 
v2 = 2



if x2>x1 and v2>v1:
    print("False")

elif (x2+v2)%(x1+v1):
    print("True")
else:
    print("FAlse")
 