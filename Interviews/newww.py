

# def decor(fun):
#     def wrapper(a,b):
#         if b<a:
#             a,b=b,a
#         return fun(a,b)
#     return wrapper

# @decor
# def akhil(l,m):
#     return l/m

# print(akhil(0,1))



a = [1,None,2,3,None,None,5,None]
# op_ls = []

# for i in range(len(a)):
#     if a[i] is not None:
#         op_ls.append(a[i])

#     else:
#         op_ls.append(op_ls[i-1])

# print(op_ls)


# res_sum = 0

# for i in range(len(a)):
#     if a[i] is not None:
#         res_sum+=a[i]
#     else:
#         a[i] = res_sum
#         res_sum = 0
# print(a)


# for i in range(len(a)):
#     if a[i] is None:
#         a[i] = a[i-1]
        

# print(a)













# marks = [{"Rajesh", 76}, {"Suresh", 56}, {"Vijay", 62}]


# for i in marks:
#     # print(i)
#     temp = list(i)
#     # print(temp[0])
#     # print(temp[1])
#     if temp[0].isnumeric():
#         print(temp[0])
#         if temp[0]>60:
#             print(temp[1])
#     else:
#         if temp[1]>60:
#             print(temp[0])

    
