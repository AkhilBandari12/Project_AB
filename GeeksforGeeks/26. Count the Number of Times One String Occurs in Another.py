s = "geeks for geeks, geeks for geeks ,geeks for geeks"

l = "geeks"

print(s.count(l))
c=0
p = s.split(" ")

for i in p:
    i = i.strip(",")
    if i == l:
        c+=1

print(c)
