##########________Even Or Odd____________##########33
n = int(input("Eneter the Range Num"))

if n%2==0:
    print(f"{n} is an Even Number")
else:
    print(f"{n} is an Odd Number")
odd_list = []
even_list = []
for i in range(n):
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Odd list : {odd_list} \n Even list : {even_list}")
