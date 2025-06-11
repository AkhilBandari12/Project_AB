# n = [x for x in range(10) if x%2==0]
# print(n)


# def func(*args, **kwargs):
#     for i,v in kwargs:
#         print(i)

# # a
# d = {1:"akhil",2:"ntt"}
# func(d)

# func()


# def decorator(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper
# @decorator
# def akhil():
#     print("helloo")
# akhil()

# nums = [1,2,3,4]
# l = list(map(lambda x:x**2,nums))
# print(l)


# n =0
# while n>0:
#     yield 


# s = "akhilbandari"

# for i in s:
#     c = s.count(i)
#     if c >1:
#         continue
#     else:
#         print(i)
#         break

# l1 = [1,2,3,4]
# l2 = [3,4,5,6]

# print(list(set(l1)&set(l2)))


# docker build -t ESICapp
# docker run -p 8000:8000 app

# file ="abc.txt"
# with open(file,"r") as f:
#     a = f.read


# import boto3

# s3_obj = boto3.client("s3",aws_acces_key_id="",aws_secret="",region_name ="us-east")

# s3_obj.upload_file("")

# teraform teragrunt