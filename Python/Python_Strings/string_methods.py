a = "akhil"

print(a.capitalize())        #Converts the first character to upper case

print(a.casefold())          #Converts string into lower case

print(a.center(20,"#") )     #Returns a centered string  
#Syntax : string.center(length, character)

print(a.count("k"))          #Returns the number of times a specified value occurs in a string

print(a.encode())            #Returns an encoded version of the string

print(a.endswith("l"))       #Returns true if the string ends with the specified value
#Syntax : string.endswith(value, start, end)

print(a.expandtabs)

sample = 'Welcome to python World'
print(sample.capitalize()) # 'Welcome to python World'


##expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

sample = 'thirty\tdays\tof\tpython'
print(sample.expandtabs())   # 'thirty  days    of      python'
print(sample.expandtabs(10)) # 'thirty    days      of        python'

#find(): Returns the index of the first occurrence of a substring, if not found returns -1

sample = 'Welcome to python World'
print(sample.find('y'))  # 5
print(sample.find('th')) # 0

#rfind(): Returns the index of the last occurrence of a substring, if not found returns -1

sample = 'Welcome to python World'
print(sample.rfind('y'))  # 16
print(sample.rfind('th')) # 17

#format(): formats string into a nicer output  
first_name = 'Akhil'
last_name = 'Bandari'
age = 30
job = 'Software'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job)
print(sentence) 


#The area of a circle
radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError. 
sample = 'Welcome to python World'
sub_string = 'da'
print(sample.index(sub_string))  # 7
print(sample.index(sub_string, 9)) # error


#rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
sample = 'Welcome to python World'
sub_string = 'da'
print(sample.rindex(sub_string))  # 7
print(sample.rindex(sub_string, 9)) # error
print(sample.rindex('on', 8)) # 19

#isalnum(): Checks alphanumeric character
sample = 'ThirtyDaysPython'
print(sample.isalnum()) # True
sample = '30DaysPython'
print(sample.isalnum()) # True
sample = 'Welcome to python World'
print(sample.isalnum()) # False, space is not an alphanumeric character
sample = 'Welcome to python World 2025'
print(sample.isalnum()) # False

#isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
sample = 'Welcome to python World'
print(sample.isalpha()) # False, space is once again excluded
sample = 'ThirtyDaysPython'
print(sample.isalpha()) # True
num = '123'
print(num.isalpha())      # False

#isdecimal(): Checks if all characters in a string are decimal (0-9)
sample = 'Welcome to python World'
print(sample.isdecimal())  # False
sample = '123'
print(sample.isdecimal())  # True
sample = '\u00B2'
print(sample.isdigit())   # False
sample = '12 3'
print(sample.isdecimal())  # False, space not allowed

#isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
sample = 'Thirty'
print(sample.isdigit()) # False
sample = '30'
print(sample.isdigit())   # True
sample = '\u00B2'
print(sample.isdigit())   # True

#isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

#isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
sample = '3Samples'
print(sample.isidentifier()) # False, because it starts with a number
sample = 'Hello_World'
print(sample.isidentifier()) # True

#islower(): Checks if all alphabet characters in the string are lowercase
sample = 'Welcome to python World'
print(sample.islower()) # True
sample = 'Welcome to python World'
print(sample.islower()) # False

#isupper(): Checks if all alphabet characters in the string are uppercase
sample = 'Welcome to python World'
print(sample.isupper()) #  False
sample = 'Welcome to python World'
print(sample.isupper()) # True

#join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

#strip(): Removes all given characters starting from the beginning and end of the string
sample = 'thirty days of pythoonnn'
print(sample.strip('noth')) # 'irty days of py'


#replace(): Replaces substring with a given string
sample = 'Welcome to python World'
print(sample.replace('python', 'coding')) # 'Welcome to coding World'

#split(): Splits the string, using given string or space as a separator
sample = 'Welcome to my World'
print(sample.split()) # ['Welcome, to, my, world']
sample = 'Welcome, to, my, world'
print(sample.split(', ')) # ['Welcome, to, my, world']


#title(): Returns a title cased string
sample = 'Welcome to python World'
print(sample.title()) # Welcome to python World

#swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
sample = 'Welcome to python World'
print(sample.swapcase())   # Welcome to python World
sample = 'Welcome to python World'
print(sample.swapcase())  # Welcome to python World

#startswith(): Checks if String Starts with the Specified String
sample = 'Welcome to python World'
print(sample.startswith('thirty')) # True
sample = '30 days of python'
print(sample.startswith('thirty')) # False