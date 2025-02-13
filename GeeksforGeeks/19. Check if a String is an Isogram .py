"""

Given a word or phrase, check if it is an isogram or not. An Isogram is a word in which no letter occurs more than once

Examples: 

Input: Machine
Output: True
Explanation: “Machine” does not have any character repeating, it is an Isogram

Input : Geek
Output : False
Explanation: “Geek” has 'e' as repeating character, it is not an Isogram


"""




def isogram(s):
    s = s.lower()
    for i  in s:
        if s.count(i)>1:
            return(False)
    return True
    
s= "Machine"
s="Geek"
print(isogram(s))