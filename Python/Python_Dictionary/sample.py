input= "SSSTTTTSSSPPPPP"
f_dict={}
output =""
for i in input:
    if i in f_dict:
        f_dict[i]+=1
    else:
        f_dict[i]=1
print(f_dict)

# for k,v in f_dict.items:
#     print((output.join(k)).join(v))