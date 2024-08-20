"""
Prime numbers are numbers greater than 1 that only have two factors, 1 and the number itself. 
This means that a prime number is only divisible by 1 and itself. 
2, 3, 5, 7, 11, 13, 17, 19, ...........

"""

# #####________Prime or Not________########

n = int(input("Enter any num"))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(f"{n} is a Prime number")
else:
    print(f"{n} is not a prime number")


########________Prime Number in a Range _________#######

lower_range = int(input("Enter starting Number"))
higher_range = int(input("Enter last Number"))

for i in range(lower_range,higher_range+1):
    count =0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=" ")


########________Prime Number Pair == Sum _________#######


lower_range = int(input("Enter starting Number"))
higher_range = int(input("Enter last Number"))
summation_number = int(input("Enter the summation number"))
list_of_prime = []
pairs_list = []
for i in range(lower_range,higher_range+1):
    count =0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        list_of_prime.append(i)
for i in list_of_prime:
    for j in range(len(list_of_prime)):
        if int(i)+int(list_of_prime[j])==summation_number:
            pairs_list.append([i,list_of_prime[j]])
print(list_of_prime)
print(pairs_list)
