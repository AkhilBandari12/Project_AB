"""


The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


"""


# s = "hello"
s = "leetcode"
lis_s = list(s)
vowels = "aeiouAEIOU"
l = len(s)


start = 0
end = l-1


while start<end:
    while start<end and lis_s[start] not in vowels:
        start+=1
    while start<end and lis_s[end] not in vowels:
        end=end-1
    lis_s[start],lis_s[end] = lis_s[end],lis_s[start]
    start+=1
    end-=1

print("".join(lis_s))

    
