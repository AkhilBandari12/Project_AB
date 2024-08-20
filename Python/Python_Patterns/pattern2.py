#         *
#       * *
#     * * *
#   * * * *
# * * * * *


num = int(input("enter num of rows"))

for i in range(num):

    for j in range(num-i-1):
        print("8",end="")
    for k in range(i+1):
        print("*",end="")
    print()
