# a = [(1,2,3), 4]
# a[0][1] = 5
# print(a)

# __init__.py vs __init__()


# l = [1,2,3,4,5]

# x =filter(lambda y:yl)
# print(x)

# t = reduce(lambda x,y:x+y,l)
# print(t)


#########   move ZEROS to last #####

# def move(l):
#     insert_pos = 0
#     for num in l:
#         if num!=0:
#             l[insert_pos]=num
#             insert_pos+=1
#     while insert_pos<len(l):
#         l[insert_pos] = 0
#         insert_pos+=1
# l = [1,2,0,0,3,0,10]
# move(l)
# print(l)



# SELECT empid COUNT(*)
# FROM Employee
# GROUP BY empid
# HAVING count(*)>1;




# SELECT dept,MAX(salary) AS max_salary
# FROM Employee
# GROUP BY dept