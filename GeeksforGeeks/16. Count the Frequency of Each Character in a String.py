"""

Input: s = “geeksforgeeks”
Output: g2 e4 k2 s2 f1 o1 r1

Input: str = “elephant”
Output: e2 l1 p1 h1 a1 n1 t1

"""


s = "geeksforgeeks"
l = []

for i in s:
    if i not in l:
        print(i+str(s.count(i)), end =" ")
        l.append(i)
    else:
        continue
