"""


Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


"""


# s = "abciiidef"
# s ="aeiou"
# s = "leetcode"
s = "weallloveyou"
k = 7

vowels = ["a","e","i","o","u"]
cou = 0
st = ""

for i in range(len(s)):
    for l in range(i,len(s)):
        temp = s[l:l+k]
        temp_cou = 0
        for j in temp:
            if j in vowels:
                temp_cou+=1
        if temp_cou>cou:
            cou = temp_cou
            st = temp
print(cou,st)