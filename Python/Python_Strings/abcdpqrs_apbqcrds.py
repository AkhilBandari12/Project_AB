first_string = str(input("Enter any string"))
second_string = str(input("Enter any string"))
combination = int(input("Enter 1 (1st on 2nd) or 2(2nd on 1st)"))

first_len = len(first_string)
second_len = len(second_string)
range_len = max(first_len,second_len)

if combination==1:
    str_list =[]
    for i in range(range_len):
        if i<first_len and i<second_len:
            str_list.append(first_string[i])
            str_list.append(second_string[i])
        elif i<first_len:
            str_list.append(first_string[i:range_len+1])
            break
        elif i<second_len:
            str_list.append(second_string[i:range_len+1])
            break
    print("".join(str_list))

if combination==2:
    str_list =[]
    for i in range(range_len):
        if i<first_len and i<second_len:
            str_list.append(second_string[i])
            str_list.append(first_string[i])

        elif i<first_len:
            str_list.append(first_string[i:range_len+1])
            break
        elif i<second_len:
            str_list.append(second_string[i:range_len+1])
            break
    print("".join(str_list))
