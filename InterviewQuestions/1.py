# print(bool(True))



# inp = "3[a]2[bc]"
#op = aaabcbc
inp = "3[a2[c]]"
# op2 = accaccacc







# inp = inp[::-1]

# print(inp)
# op = ""
# temp = ""
# for i in inp:

#     if i in ["[","]"]:
#         continue
#     elif i.isalpha():
#         temp+=i
#     elif i.isnumeric():
#         p = int(i)*temp
#         op+=p
#         temp=""


# print(op[::-1])



def decode_string(s):
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == "]":
            last_string, num = stack.pop()
            current_string = last_string + num * current_string
        else:
            current_string += char

    return current_string


inp = "3[a2[c]]"
output = decode_string(inp)
print(output) 