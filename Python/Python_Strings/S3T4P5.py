input = str(input("Enter the string with numbers : "))
output = []
for i in input:
    print(i)
    if i.isdigit():
        num = int(i)
        # print(f"num : {num}")
        slice = int(input.index(i))
        print(f"Slicepoint {slice}")
        print(input[slice-1]*num)
        output.append(input[slice-1]*num)

print("".join(output))