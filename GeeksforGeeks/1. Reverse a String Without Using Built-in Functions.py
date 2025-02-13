
s = "Akhil"

print("".join(reversed(s)))

print(s[::-1])
op =""
for i in range(len(s)-1,0-1,-1):
    # print(i)
    op+=s[i]

print(op)