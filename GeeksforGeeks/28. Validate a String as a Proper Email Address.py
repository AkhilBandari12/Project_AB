from email_validator import validate_email,EmailNotValidError


# def check(email):
#     try:
#       # validate and get info
#         v = validate_email(email) 
#         # replace with normalized form
#         email = v["email"]  
#         print("True")
#     except EmailNotValidError as e:
#         # email is not valid, exception message is human-readable
#         print(str(e))

# check("my.ownsite@our-earth.org")
# check("ankitrai326@ff.com")


import re

email = "my.ownsite@our-earth.org"
valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

print("Valid email address." if valid else "Invalid email address.")