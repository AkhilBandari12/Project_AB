"""

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"


"""

# str1 = "ABCABC"
# str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"

# str1 = "LEET"
# str2 = "CODE"

# str1 = "GFGGFG"
# str2 = "GFGGFGGFGGFG"           #"GFGGFG"     

# if len(str1) < len(str2):
#     divisor= str1
#     factor = str2
# else:
#     divisor =  str2 
#     factor = str1
# op_str = ""

# for i in range(len(divisor)+1):
#     for k in range(len(factor)+1):
#         if divisor[i:k] in factor and len(divisor[i:k]) > len(op_str):
#             op_str = divisor[i:k]
# print(op_str)

def gcd(a,b):
    n = min(a,b)
    # m =max(a,b)
    while n:
        if a % n == 0 and b % n == 0:
            break
        n-= 1
    return n
temp = str1 + str2 
if str1 + str2 == str2 + str1:
    # print("")
    print(temp[0:gcd(len(str1),len(str2))])
else:
    print("")
