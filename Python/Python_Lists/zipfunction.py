input1 = list(input("Enter the first string"))
input2 = list(input("Enter the second string"))


print("".join([f"{m}{n}" for m,n in zip(input1,input2)]))