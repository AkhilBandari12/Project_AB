"""

Pascal Casing - capitalizes each word:   ----  ThisShouldBePascalCase

Camel Casing - is similiar to pascal case but the first word is not capitalized:     -----  thisShouldBeCamelCase


"""
s = 'This string is converted to camelCase'

l = s.split(" ")

op = l[0].lower()
for i in l[1:]:
    # print(i)
    op+=i.capitalize()


print(op)

