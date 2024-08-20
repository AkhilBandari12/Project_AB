s = input("Enter any string ")
s_len = len(s)
s_list = []
default_len = 0
op_str = ""

for i in range(s_len+1):
    for j in range(i,s_len+1):
        temp = s[i:j]
        if temp == temp[::-1] and temp!="" and len(temp)>1:
            s_list.append(s[i:j])
print(f"the pallendromes in the given string are :  {s_list}")
for k in s_list:
    if len(k)>default_len:
        default_len = len(k)
        op_str=k

print(f"the logest pallendrome in the given string is : {op_str} & lenght is {len(op_str)}")

# oplist = [x for x in s_list if len(x)==default_len]
# # print(oplist)
# if len(oplist)==1:
#     print(f"the logest pallendrome in the given string is : {op_str} & lenght is {len(op_str)}")
# else:
#     print(f"the logest pallendromes in the given string is : {oplist} & lenght is {len(op_str)}")



