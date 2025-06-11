
#fibonacci series
# a=0
# b=1

# for i in range(10):
#     print(a,end=" ")
#     c=a+b
#     a,b = b,c


# l =[2,3,4,5,6,9,10]
# f = l[0]
# la = l[-1]


# l[0],l[-1] = la,f

# print(l)


# max Num
# numberList = [15, 85, 35, 89, 125]
# ma_num = numberList[0]

# for i in numberList:
#     if i>ma_num:
#         ma_num=i


# print(ma_num)


# Reverse of name
# a = "Akhil"
# op = ""
# for i in range(len(a)):
#     op+=a[len(a)-i-1]

# print(op)

# #sequel 

# SELECT max(salary) As second_max_salary
# from emp_dept
# where salary <(select max(salary) from empl);


# SELECT 
#     order_date,
#     shipped_date,
#     datediff(shipped_date,order_date) as days

# FROM order;

# person with less than 2 years
# SELECT
#     e.salary,
#     e.hire_date,
#     d.department
# FROM
#     employee e
# JOIN
#     department d ON e.dep_id =d.dep_id
# where
#     e.hire_date <= DATEADD(YEAR, -2, GETDATE());


# average salary 
# SELECT
#     AVG(e.salary) as avg_sal,
#     d.dept_name
# FROM
#     employee e
# JOIN
#     department d ON e.dep_id =d.dep_id
# where
#     e.hire_date <= DATEADD(YEAR, -2, GETDATE());
# groupby
#     d.dept_name;