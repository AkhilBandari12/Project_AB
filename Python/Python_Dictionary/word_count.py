"""


Case 1:
test_string:hello world program world test
{'test': 1, 'world': 2, 'program': 1, 'hello': 1}
 
Case 2:
test_string:orange banana apple apple orange pineapple
{'orange': 2, 'pineapple': 1, 'banana': 1, 'apple': 2}


"""


# test_string=input("Enter string:")
test_string = "hello world program world test"

l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))