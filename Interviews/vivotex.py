"""
coins = [1, 3, 4, 5]
amount = 7

o/p - [3,4],[1,1,5]


"""

# coins = [1, 3, 4, 5]
# amount = 7

# op_list = []
# for i in range(len(coins)-1):
#     if coins[i]+coins[i+1]==amount:
#         op_list.append([coins[i],coins[i+1]])

# print(op_list)


# string = "hello"
# shift_amount = 3

# string = "hello"
 
# shift_amount = 3
 
# o/p = khoor
 
# abc, 3


# String = "HelloWorld"
# #op HeWrd

# string_list = list(String)
# op = ""
# for i in string_list:
#     if string_list.count(i)==1:
#         op+=i

# print(op)


# ind the top 3 highest-paid salaries employees in each department

# Employee table :
# Emp ID , Emp Name, Salary, Emp designation 

# department table:
# Depart Id and departname



# SELECT *
# FROM (
#     SELECT * DENSERANK() OVER (ORDERED By Salary DESC) AS sal_Rank
#     FROM Employee
# ) 
# Where sal_Rank <=3

# from collections import defaultdict
# li = [1,2,3,4]
# # dic = dict()

# # for i in range(len(list)-1):
# #     dic[i]=li[i]

# # print(dic)

# d = defaultdict(li)

# for i in  li:
#     d.append(i)



"""
develop an endpoint "GET v1/data?a1=3&b2=4&c17=3  and the list continues" here the params keys are not constant and the number of params we are getting is also  not constants

    task : print all the params coming as part of the endpoint along with the values
 """

# Model.py
# from django.db import models

# Class User(models.model):
#     name = 
#     mailid = 

# UNIT TEST -- CASES


from rest_framework.decorator import APIview

@APIview["GET"]
def get_object(request):
    users = user.object.all()
    return list(users)
