"""


For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"



"""

def create_manual_number_to_letter_dict():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number_to_letter_dict = {i + 1: letter for i, letter in enumerate(letters)}
    return number_to_letter_dict
number_to_letter_dict = create_manual_number_to_letter_dict()
print(number_to_letter_dict)


columnNumber = 1

def number_to_column(n, number_to_letter_dict):
    column_name = ""
    while n > 0:
        print(n)
        n -= 1  
        print(n)
        remainder = n % 26
        print(remainder)
        column_name = number_to_letter_dict[remainder + 1] + column_name
        print(column_name)
        n = n // 26
        print(n)
    return column_name

number_to_letter_dict = create_manual_number_to_letter_dict()

# Examples
# print(number_to_column(1, number_to_letter_dict))    # Output: A
print(number_to_column(28, number_to_letter_dict))   # Output: AB
# print(number_to_column(701, number_to_letter_dict))  # Output: ZY
# print(number_to_column(1430, number_to_letter_dict)) # Output: BBZ