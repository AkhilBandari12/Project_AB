

s = "Hello, World! Python is amazing.$$%#@#@@#$%^&*"

# import string
# translator = str.maketrans('', '', string.punctuation)

# clean_text = s.translate(translator)
# print(clean_text)


op = ""

for i in s:
    if i.isalnum():
        op+=i
    elif i.isspace():
        op+=i

print(op)