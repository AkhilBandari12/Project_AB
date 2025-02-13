s = "Akhil Bandari"

s = s.lower().strip()
vow_cou = 0
conse_cou = 0 
special_cou =0
for i in s:
    if i.isalpha():
        if i in ['a','e','i','o','u']:
            vow_cou+=1
        else:
            conse_cou+=1
    else:
        special_cou+=1
print(vow_cou,conse_cou,special_cou)
