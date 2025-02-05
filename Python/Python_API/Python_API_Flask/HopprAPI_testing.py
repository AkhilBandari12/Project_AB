import requests

url = "https://rpabot.buzzworks.com/generate_id_card/"
data = {
    "name": "Akhil",
    "employee_id": "123456",
    "designation": "Python Developer",
    "DOJ": "2024-02-07",
    "department": "buzzworks",
    "location": "Karimnagar",
    "Blood_Group": "O+",
    "Emergency_Contact_No.": "7989172960",
    "legal_entity": "RBL"
}
image_path = "/home/buzzadmin/Documents/Desktop/Git_Clone_Backup/Backup_Automation BOTs/Prod_Server_code_Backup/idcardgenerator/image.jpg"
files = {
    "photo_path": open(image_path, "rb")  
}

response = requests.post(url, files=files, data=data)

print(response.status_code)
# print(response.text)
