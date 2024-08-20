inp = input("Enter any string")
temp = list(set(inp))
# print(temp)
outlist=[]
for i in temp:
    count=0
    for j in inp:
        if i==j:
            count+=1 
    # print(count)
    outlist.append([i,count])
    # print(outlist)
res = ''.join([f'{m}{n}' for m, n in outlist])

print(res)


