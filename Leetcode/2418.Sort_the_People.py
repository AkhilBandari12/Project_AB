"""

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.


"""
names = ["Mary","John","Emma"]
heights = [180,165,170]

# names = ["Alice","Bob","Bob"]
# heights = [155,185,150]
# op_dic = {}
# d = zip(names,heights)

# for k,v in d:
#     if k not in op_dic or v>op_dic[k]:
#         op_dic[k] = v
# print(op_dic)

# name_list = sorted(op_dic, key=op_dic.get, reverse=True)
# print(name_list)

# dic1 = {k:v for k,v in d  }
# print(dic1)
# dic = {k: v for k, v in sorted(dic1.items(), key=lambda item: item[1],reverse=True)}
# print(dic)
# op_ls = list(dic.keys())
# print(op_ls)

ip_ls = list(zip(names, heights))

sort_ls = sorted(ip_ls, key=lambda x: x[1], reverse=True)

op_ls = [k for k, v in sort_ls]

print(op_ls) 






