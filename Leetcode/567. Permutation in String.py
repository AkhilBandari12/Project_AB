"""


Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false



"""

from itertools import permutations
# s1 = "ab"
# s2 = "eidbaooo"


s1 ="dinitrophenylhydrazine"
s2 ="acetylphenylhydrazine"


perm_list = ["".join(p) for p in permutations(s1)]

for i in perm_list:
    if s2.__contains__(i):
        print(True)

print(False)

















