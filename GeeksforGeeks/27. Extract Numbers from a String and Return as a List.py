

s  = "There are 2 apples for 4 persons"

l = s.split(" ")


for i in l:
    # print(i)
    if i.isdigit():
        print(i,end=" ")