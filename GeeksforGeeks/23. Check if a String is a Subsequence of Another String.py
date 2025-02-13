"""
Input: s1 = “AXY”, s2 = “ADXCPY”
Output: True 
All characters of s1 are in s2 in the same order


Input: s1 = “AXY”, s2 = “YADXCP”
Output: False 
All characters are present, but order is not same.


Input: s1 = “gksrek”, s2 = “geeksforgeeks”
Output: True

"""

s1 = "AXY" 
s2 = "ADXCP"


for i in s1:
    print(i)
    print(s2.count(i))
    if s2.count(i)>0:
        continue
    else:
        print(False)
        # break
print(True)