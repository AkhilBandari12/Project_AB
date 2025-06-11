# # # #write a sample decorator 

# # # def decorator(func):
  
# # #     def wrapper():
# # #         print("Before calling the function.")
# # #         func()
# # #         print("After calling the function.")
# # #     return wrapper

# # # @decorator

# # # def greet():
# # #     print("Hello, World!")

# # # greet()




# # # List sorting without using inbuilt functions

# # l1=[76, 23, 45, 12, 54, 9] 
# # print("Original List:", l1)

# # # sorting list using nested loops
# # for i in range(0, len(l1)):
# #     for j in range(i+1, len(l1)):
# #         if l1[i] >= l1[j]:
# #             l1[i], l1[j] = l1[j],l1[i]

# # # sorted list
# # print("Sorted List", l1) 


# # # Full flattening using recursion
# # def flatten(lst):
# #     result = []
# #     for item in lst:
# #         if isinstance(item, list):
# #             result.extend(flatten(item))
# #         else:
# #             result.append(item)
# #     return result


    
# # l = [6, 3, [-7, -8, 1], 12, [[1, 2, 0], 65]]
# # print(flatten(l))  # [6, 3, -7, -8, 1, 12, 1, 2, 0, 65]

# l=[1,2,3]
# def fun(l):
#     l.append(10) 
# fun(l)
# print(l)


# a = 10
# def fun():
#     # global a
#     a = 15

# fun()
# print(a)





#s = """"""""""""""""""""""""""



#diamond problem
# class A:
#     def fun(self):
#         pass
# class B(A):
#     def fun(self):
#         pass
# class C(A):
#     def fun(self):
#         pass
# class D(B,C):
#     pass



# input  = [{)(()}] 
# output = [[], {},(),(,)]


# s = "AaaBbcbbdddAaaa"
# # op = A1a2B1c1b2d3A1a3
# count = 1
# op_strt = ""
# for i in range(len(s)-1):
#     print(i)
#     temp = s[i] 
#     if temp == s[i+1]:
#         count+=1
#     else:
#         op_strt = op_strt+temp+str(count)
#         count= 1

# print(op_strt)













# def decorat(func):
#     def wrapper(*args):
#         # st = st.upper()
#         return func(*args.upper())
#     return wrapper


# @decorat
# def akhil():
#     return "Akhil"



# print(akhil())






# # elements between 2 lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
 
# # => [4, 5]

list3 = [x for x in list1 if x in list2]
print(list3)
# # s= set(list1)
# # s1 = set(list2)

# # print(list(s&s1))

# new_list = []
# for i in list1:
#     if i in list2:
#         new_list.append(i)

# print(new_list)



# Create a list having every tenth element from the given list
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
 
list4 = [j for i,j in enumerate(mylist) if i> 0 and (i+1)%10 == 0]
print(list4)
# [9, 19, 29]
# new_list = []
# for i in range(1,len(mylist)):
#     if i%10==0:
#         new_list.append(mylist[i-1])

# print(new_list)


# employee = {
#     'first_name' : ['David', 'John', 'Olivia', 'Steve'], 
#     'last_name' : ['Miller', 'Doe', 'Vats', 'Smith'], 
#     'salary' : [15000, 20000, 25000, 22000], 
#     'department' : ['IT', 'Account', 'IT', 'Account']
# }

# import pandas as pd

# df = pd.DataFrame(employee)




# Given a list of strings, group the anagrams together. You need to return a list of lists where each sublist contains words that are anagrams of each other.
 
# Input                        ["eat","tea","tan","ate","nat","bat"]

# Expected Output    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
 


# l = ["eat","tea","tan","ate","nat","bat"]

# op_list = []
# temp = sorted(l)[0]
# print(temp)

# for i in l:
#     if temp == sorted(i):
#         op_list.append("".join[temp])
#     else:
#         temp = sorted(i)
#         op_list.append([temp])

# print(op_list)




# employee = {
#     'first_name' : ['David', 'John', 'Olivia', 'Steve'], 
#     'last_name' : ['Miller', 'Doe', 'Vats', 'Smith'], 
#     'salary' : [15000, 20000, 25000, 22000], 
#     'department' : ['IT', 'Account', 'IT', 'Account']
# }

# import pandas as pd

# df = pd.DataFrame(employee)

# # df['name'] = df['first_name']+' '+df['last_name']

# # # print(df)
# df.drop(['first_name'], axis=1, inplace=True)
# print(df)
# # print(df.drop(['first_name'],axis=1)
# # )

# # print(df)

# max_df =  df.groupby('department')['salary'].max()

# print(max_df)



def group_anagrams(words):
    anagram_map = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]
        print(anagram_map)
    return list(anagram_map.values())

# Example usage
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input_list)
print(output)










