"""
nput: s1 = “abcd”, s2 = “cdab”
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.


Input: s1 = “aab”, s2 = “aba”
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.


Input: s1 = “abcd”, s2 = “acbd”
Output: false
Explanation: Strings are not rotations of each other.


"""

# s1 = "abcd"
# s2 = "cdab"

s1 = "abcd"
s2 = "acbd"

l = len(s1)


for i in range(l):
    if s1==s2:
        print(True)
    else:
        s1 = s1[-1]+s1[:-1]
print(False)