# loans = [
#     {"loan_number": "LN001", "borrower": "Alice", "amount": 10000, "status": "Active"},
#     {"loan_number": "LN002", "borrower": "Bob", "amount": 15000, "status": "Closed"},
# ]


# def loan_numb(n):
#     for i in loans:
#         if i["loan_number"]==n:
#             return i
# print(loan_numb("LN001"))


# products = [
#     {"name": "Laptop", "category": "Electronics", "price": 1200},
#     {"name": "T-shirt", "category": "Clothing", "price": 20},
#     {"name": "Phone", "category": "Electronics", "price": 800}
# ]
 
# for i in products:
#     if i["category"]=="Electronics":
#         print(i["name"])



# Dept
# dept_id dept_name dept_code
# 1       Tech        001
# 2       HR           002
# 3      Finance      003
 
# Employee
# emp_id emp_name emp_salary emp_dept
# 1       Ram    120,000         1
# 2.      John        130,000         1
# 3.      Anjali        125,000         2


# SELECT Employee.empname,dept.dept_name 
# FROM Employee
# JOIN Dept ON Employee.emp_dept =Depar.depar_id 

# data = {
#     "product_id":["P01","P02","P03","P01","P02"],
#     "quantity":[5,10,8,2,4],
#     "price": [100,50,20,150,150],
#     "catergory":["Electronics","clothing","groceries","Electronics","clothing"],
# }

# import pandas as pd 

# df = pd.DataFrame(data)
# print(df)

# df ["sales"]=df["quantity"]*df["price"]

# total = df["quantity"]sum()