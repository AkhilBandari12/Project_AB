s = "Akhil Bandari"


print(s.swapcase())

op = ''
for i in s:
    if i.isalpha():
        if i.lower():
            op+=i.upper()
        elif i.upper():
            op+=i.lower()
    else:
        op+=i
print(op)
