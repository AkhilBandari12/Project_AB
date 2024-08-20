"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

"""


s = "()"

if (s.__contains__("(") and s.__contains__(")")) or (s.__contains__("{") and s.__contains__("}")) or (s.__contains__("[") and s.__contains__("]")) :
    print(True)
