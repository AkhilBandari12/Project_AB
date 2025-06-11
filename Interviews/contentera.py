# l = [1,2,3,4,5]

# print(l[2:4])


# """"
# If two students get same rank, followed by student shouldn’t get the consecutive rank (Example: Student 1, Student 2 got rank 1, Student 3 should get rank as 3 not 2.
#  """

# marks = [90,80,75,80,65]


# uniqu = sorted(set(marks))

# # print(uniqu)
# rank_dict = {mark:x+1 for x,mark in enumerate(uniqu)}
# print(rank_dict)

# # print(rank_dict)

# for k in marks:
#     print(f"{k} rank {rank_dict[k]}")






# You are given a bracket sequence of length N𝑁 consisting of only '(' and ')'. Your task is to output an array of length N𝑁.
#  The ith𝑖𝑡ℎ element in the array must be equal to the index of the corresponding bracket in the sequence of the ith𝑖𝑡ℎ bracket. 
#  If there is no corresponding bracket then the value in the array at that position should be -1. Please look at the sample testcase for a better understanding.
 
# Sample Input:
 
# Example1:  
 
# Input: (())()
 
# Output: 3 2 1 0 5 4
 
# Example 2:
 
# Input: )((()
 
# Output: -1 -1 -1 4 3


def match_colo(s):
    stack = []
    result =[-1]*len(s)
    for i,ch in enumerate(s):
        if ch =='(':
            stack.append(i)
        elif ch ==')':
            if stack:
                opening_index = stack.pop()
                result[opening_index]=i+1
                result[i]= opening_index+1

            else:
                result[i]=-1        
    return result

t =  ")((()"

print(match_colo(t))

