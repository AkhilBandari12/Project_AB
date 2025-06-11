# a = lambda x,y : x+y

# a(5,3)

# def dec(fun):
#     def wrapper(:
#         print("abc")
#         fun()
#         )

# def decorat(fun):
#     def wrapper(a,b):
#         if a<b:
#             a,b=b,a
#         return fun(a,b)
#     return wrapper

# @decorat
# def division(x,y):
#     return x/y


# res = division(3,5)
# print(res)


# st ="[({a+b} + {c+d})]"
# st="({a+b)} + {c+d})"
# st= "[({a+b} + {c+d})][)"


# for i in st:
#     if i == "}":


# for i in range(len(st)):
#     if st[i]=="]":
#         st

# p = {')':'(','}':'{','[':']'}

# start = set(p.values())
# end = set(p.keys())
# stack = []

# for idx, i in enumerate(st):
#     if i in start:
#         stack.append((i,idx))
#     elif i in end:
#         if not stack:
#             print("Unbalanced")
#         else:
#             l,m = stack.pop()
#             if 

# print(stack)

# input - 
# output - a3b2c1d1e4f1g1

# input - aaabbcdeeeeaaaafgc
# Regulla Sanjay
# 6:43 PM
# output - a3b2c1d1e4a4f1g1c1


# inp_str = "aaabbcdeeeeaaaafgc"

# # op_str =""
# res = []
# count = 1

# for i in range(1,len(inp_str)):
#     if inp_str[i] == inp_str[i-1]:
#         # temp = inp_str[i]
#         count+=1
#     else:
#         # op_str+=temp+str(count)
#         res.append(inp_str[i-1]+str(count))
#         count = 1
# res.append(inp_str[-1]+str(count))

# print("".join(res))


# fibo = 1,1,2,3,5
# a,b = 0,1

# for i in range(10):
#     print(a, end=" ")
#     a,b = b,a+b
    

# """Regulla Sanjay
# 6:22 PM
# balanced - [({a+b} + {c+d})]
# Unbalanced - [({a+b} + {c+d})]]
# balanced - [({a+b} + {c+d})][)
# unbalanced - [({a+b} + {c+d})][)
# Regulla Sanjay
# 6:23 PM
# unbalanced - [({a+b}} + {c+d})]{
# unbalanced - [({a+b)} + {c+d})
# Regulla Sanjay
# 6:24 PM
# unbalanced - [({a+b)} + {c+d})]
# Regulla Sanjay
# 6:26 PM
# -----------
# balanced - [({a+b} + {c+d})]
# unbalanced - [({a+b)} + {c+d})
# unbalanced - [({a+b} + {c+d})][)
# Regulla Sanjay
# 6:37 PM
# input - aaabbcdeeeefg
# Regulla Sanjay
# 6:42 PM
# output - a3b2c1d1e4f1g1
# input - aaabbcdeeeeaaaafgc
# Regulla Sanjay
# 6:43 PM
# output - a3b2c1d1e4a4f1g1c1
# Regulla Sanjay
# 6:56 PM
# What does *args and **kwargs mean?
# Technical Discussion - Akhil Bandari - Python Dev"""