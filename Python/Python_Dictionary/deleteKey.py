"""

The program takes a dictionary and removes a given key from the dictionary.


"""



d = {'a':1,'b':2,'c':3,'d':4}
print(d)
key=input("Enter the key to delete(a-d):")
if key in d: 
    del d[key]
else:
    print("Key not found!")
    exit(0)
print(f"Updated dictionary {d}")