n = int(input("Enter the number for which the table should be displayed : "))
m = int(input("Enter the number till which the table should be displayed : "))

for i in range(1,m+1):
    print(f"{n}*{i} = {i*n}")
