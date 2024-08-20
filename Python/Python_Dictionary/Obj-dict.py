"""

Problem Description
The program forms a dictionary from an object of a class.


"""


class A(object):  
     def __init__(self):  
         self.A=1  
         self.B=2  
obj=A()  
print(obj.__dict__)