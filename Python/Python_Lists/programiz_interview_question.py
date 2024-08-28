"""


Please find the count of number of times each word is getting repeated. 

a = "Sabyasachi, Techno Exponent Techno I sabyasachi"


"""

a = "Sabyasachi, Techno Exponent Techno I sabyasachi"
#sorted(a_list)
a_list = a.split(" ")
# lowercaselist = [x.lower() for x in a_list ]

output_list = []
for i in a_list:
    # print(i)
    temp =""
    for j in i:
        print(j)
        if j.isalpha():
            temp+=j
    output_list.append(temp.lower())
print(output_list)

for k in set(output_list):
    print(k.capitalize(),output_list.count(k))