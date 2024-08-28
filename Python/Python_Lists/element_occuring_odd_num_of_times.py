
def find_odd_occurring(alist):
    """Return the element that occurs odd number of times in alist.
 
    alist is a list in which all elements except one element occurs an even
    number of times.
    """
    ans = 0
 
    for element in alist:
        ans ^= element
 
    return ans
 
 
alist = input('Enter the list: ').split()
alist = [int(i) for i in alist]
ans = find_odd_occurring(alist)
print('The element that occurs odd number of times:', ans)