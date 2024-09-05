import pandas as pd
import psycopg2

#Load Excel data
file_path = '/home/buzzadmin/Downloads/IDFC_Dummy_data.xlsx'
excel_data = pd.read_excel(file_path)

#Connect to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="newpassword"
)
cursor = connection.cursor()

#Insert Query into the database
for index, row in excel_data.iterrows():
    cursor.execute(
        'INSERT INTO e_portal ("Aadhar_Number", "Pan_Number") VALUES (%s, %s)',
        (row['Aadhar Number'], row['Pan No'])
    )

# #Insert Query into the database
# for index, row in excel_data.iterrows():
#     cursor.execute(
#         "INSERT INTO e_portal ("Aadhar_Number", "Pan_Number") VALUES (%s, %s, %s)",
#         (row['ExcelColumn1'], row['ExcelColumn2'], row['ExcelColumn3'])
    # )


#close connection
connection.commit()
cursor.close()
connection.close()