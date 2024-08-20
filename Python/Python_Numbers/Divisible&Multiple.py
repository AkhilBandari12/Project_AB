"""
numbers which are divisible by n and multiple of m in a given range of numbers.

"""


lower_range = int(input("Enter the starting range number : "))
upper_range = int(input("enter the ending range number : "))
n = int(input("Enter the Divisible number : "))
m = int(input("Enter the Multiple number : "))
op_list= []
for i in range(lower_range,upper_range):
    if i%n==0 and i%m==0:
        op_list.append(i)
print(f"The numbers which are divisible by {n} and multiple of {m} are as follows \n {op_list}")