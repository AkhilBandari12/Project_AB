"""

The program takes two lists and maps two lists into a dictionary.

"""

lis1 = [1,2,3,4,5]
lis2 = ["A","B",'C',"D","E","F"]

dic = dict(zip(lis1,lis2))
print(dic)