"""
5.Write a Python program to find a missing number from a list
Input : [1,2,3,4,6,7,8]
"""
a = [1,2,3,4,6,7,8]
missing = sum(xrange(a[0],a[-1]+1)) - sum(a)
print(missing)
