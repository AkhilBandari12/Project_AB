"""
The year should be divisible by 4.
If the year is divisible by 100, it should also be divisible by 400.

"""


year = int(input("Enter any year"))
if(year%4==0 and year%100!=0 or year%400==0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} isn't a leap year!")