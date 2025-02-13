"""

Given a string s and an integer d, the task is to left rotate the string by d positions.

Examples:

Input: s = “GeeksforGeeks”, d = 2
Output: “eksforGeeksGe”  
Explanation: After the first rotation, string s becomes “eeksforGeeksG” and after the second rotation, it becomes “eksforGeeksGe”.


Input: s = “qwertyu”, d = 2 
Output: “ertyuqw” 
Explanation: After the first rotation, string s becomes “wertyuq” and after the second rotation, it becomes “ertyuqw”.


"""

# s = "GeeksforGeeks"
# d = 3

s = "qwertyu"
d = 2 

op = s[d::]+s[:d]
print(op)