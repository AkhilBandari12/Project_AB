"""
Input  : Geeks for Geeks
Output : for

Input  : Hello Geeks
Output : HoGks

"""


s = "Geeks for Geeks"

op= ""
for i in s:
    if i not in op and s.count(i)<=1 :
        op+=i

print(op)