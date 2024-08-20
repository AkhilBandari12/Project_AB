"""

The program takes two dictionaries and concatenates them into one dictionary.

"""


d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)