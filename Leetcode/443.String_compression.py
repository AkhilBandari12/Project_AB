"""

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".



"""

# chars = ["a","a","b","b","c","c","c"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","a","b","b","a","a"]
# chars = ["A"]

op_str = ''
# for i in range(len(chars)):
#     if chars

i = 0 
pointer = 0
while i < len(chars):
    c = 1
    string = chars[i]
    while i+1 < len(chars) and string == chars[i+1]:
        c+=1
    chars[pointer] = string
    if c>1:
        s = str(c)



       

















# ip_ls = list(sorted(set(chars)))
# op_str = ""
# for i in ip_ls:
#     cou = chars.count(i)
#     if cou>1:
#         op_str+= i+str(cou)
#     else:
#         op_str+=i
# chars[0:len(chars)] = list(op_str)
# # chars = list(op_str)
# print(chars)
# print(len(chars))


# # ip_ls = list(sorted(set(chars)))
# # print(ip_ls)
# # op_str = ""
# # for i in ip_ls:
# #     cou = chars.count(i)
# #     if cou>1:
# #         op_str+= i+str(cou)
# #     else:
# #         op_str+=i
# # print(list(op_str))
# # print(len(op_str))