# st1 = "geeks"
# st2 = "forgeeks"

st1 = "hello"
st2 = "geeks"

op = ""

for i in range(len(st1)):
    op+=st1[i]
    op+=st2[i]

op+=st2[len(st1)::]

print(op)