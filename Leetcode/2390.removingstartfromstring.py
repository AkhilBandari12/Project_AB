
# s = "erase*****"
# res = ""

# for i in range(len(l)):
# for i in s:
#     if i == "*":
#         ind = i.index()
#         s.replac

# for i in ls:
#     print(i)
#     if i == '*':
#         ind = ls.index('*')
#         print(ind)
#         ls.pop(ind)
#         ls.pop(ind-1)
# print(ls)

# l_len = len(s)
# for i in range(l_len):
#     print(i)
#     if ls[i]=='*':
#         ls.pop(i)
#         ls.pop(i-1)
#         l_len -= 2

# print(ls)


# s = "leet**cod*e"
# print(len(s))
# ls = list(s)
# print(len(ls))
# i = 0
# while '*' in ls:
#     if ls[i] == '*':
#         ls.pop(i)
#         ls.pop(i-1)
#         print
#         i += 1
#     else:
#         i += 1
# print(ls)

# s = "leet**cod*e"
# flag = s.isalpha
# print(flag)
# ls = list(s)
# for i in range(len(s)):
#     while flag=="False":
#         c = s.find("*")
#         s[c-1:c]=""

# print(s)

s = "leet**cod*e"
ls = []
for i in s:
    print(i)
    if i == '*':
        if ls:
            print(f"list : {ls}")
            ls.pop() 
    else:
        ls.append(i)
print( "".join(ls))





# s = "erase*****"

# ls = list(s)
# cou = s.count("*")
# for i in range(cou):
#     for j in ls:
#         if j == "*":
#             ind = ls.index(j)
#             ls.pop(ind)
#             ls.pop(ind-1)
# print("".join(ls))
