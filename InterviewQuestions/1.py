# print(bool(True))



inp = "3[a]2[bc]"
#op = aaabcbc
# inp2 = "3[a2[c]]"
#op2 = accaccacc







inp = inp[::-1]

print(inp)
op = ""
temp = ""
for i in inp:

    if i in ["[","]"]:
        continue
    elif i.isalpha():
        temp+=i
    elif i.isnumeric():
        p = int(i)*temp
        op+=p
        temp=""


print(op[::-1])