"""

Input : s = “geeksforgeeks”
        c = 'e'
Output : s = “gksforgks”

Input : s = “geeksforgeeks”
        c = 'g'
Output : s = “eeksforeeks”

Input : s = “geeksforgeeks”
        c = 'k'
Output : s = “geesforgees”


"""

s = "geeksforgeeks"
c = "k"

op = ""
for i in s:
    if i == c:
        continue
    else:
        op+=i
print(op)