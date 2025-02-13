s = "Geeksforgeeks is best Computer Science Portal"


res = len(s.split())
print(res)
print(len(s))


import re 
res = len(re.findall(r'\w+', s))

print(res)

