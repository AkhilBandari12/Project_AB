
# EmpID, EmpName, ManagerID
# (101, 'Alice Smith', NULL)
# (102, 'Bob Johnson', 101)
# (103, 'Charlie Brown', 101)
# (104, 'David Lee', 102)
# (105, 'Eve Davis', 102)
# (106, 'Frank White', 103)
# (107, 'Grace Miller', 104)


# SELECT
#     m.EmpName as manager_name,
#     e.emmName as employe_name
# FROM 
#     employee
# LEFT JOIN 
#     Employee m ON e.ManagerID=m.EmpID
# WHERE 
#     e.managerID is NOT NULL;


sales_data = {
        'Region': ['East', 'West', 'East', 'South', 'West', 'East'],
        'Amount': [100, 150, 200, 50, 120, 80]
    }

import pandas as pd


df = pd.DataFrame(sales_data)
su_by_region  = df.groupby("region")["Amount"].sum()