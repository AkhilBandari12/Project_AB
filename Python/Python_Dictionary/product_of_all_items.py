"""

The program takes a dictionary and multiplies all the items in the dictionary.


"""




d={'A':10,'B':10,'C':239}
# d ={1:5,2:6}
tot=1
for i in d:    
    print(i)
    tot=tot*d[i]
print(tot)