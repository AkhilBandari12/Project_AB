"""
Input: s = "the sky is blue"
Output: "blue is sky the"

"""

# s = "the sky is blue"
s = "  hello world  "

ls = s.split(" ")
# print(ls)
op_ls =[]

for i in reversed(ls):
    print(i)
    if  i.isalnum():
        # print(op_ls)
        op_ls.append(i)

print(" ".join(op_ls))