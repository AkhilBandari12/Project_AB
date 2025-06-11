#veiws.py

import hashlib


def post (request):
    user = request.data.get('username')
    pswd = request.data.get('password')
    if user:
        login(request,user)
        request.session.set_expiry(300)
        return("the seesion started")

def password(request):
    pswd = request.data.get('password')
    enc_pswd = hashlib.sha256(pswd.encode())

    return(enc_pswd)



# urls.py

urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view(),name="getting Token),
    path('api/password/',password.as_view(),name = "password_protected),

]

# Response_Satus : 

import requests

if tokenresponse.code ==200:
    token = tokenresponse.json().get("token")


headers = {'Authorization':f"Bearer+{token}"}
url = "localhost/api/password"
pswd = "Some random password"





# 
# select department , max(salary) as highest_salary
# FROM employee
# group by department;



# slect * from (
#     selct*,
#  Dinse_rank() over (parttion by department order by salary DESC) as rank_sal
#  From employee)
#  sub
#  where rank_sal=3;