li=[{"name":"ravi", "age":30}, {"name":"naveen", "age":25}]

op_list = []
# age_list = []
for i in li:
    # age_list.append(i['age'])
    op_list = list(sorted(li.item()))

# print(sorted(li))


op_list = list(sorted(li.item()))

# for k in age_list:
#     # op.append({})
#     if li['age']==k:
#         # temp = 
#     # op_list.append()


# def decorator(func):
#     def wrapper(s):
#         if s =="Akhil":
#             return func(a="Akhil")

#         else:
#             return func()
#     return wrapper

# @decorator
# def test(a=""):
#     return a+"Hii"

# a = input("Enter Any name")

# print(test(a))