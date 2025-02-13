s = "abcabacabacaab"

op = ''

for i in range(len(s)):
    temp = ""
    for j in range(i,len(s)):
        if s[j] not in temp:
            temp+=s[j]
        else:
            break
    # print(temp)
    if len(temp)>len(op):
        op = temp
print(len(op))