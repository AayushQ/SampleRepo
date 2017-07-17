"""
6. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
"""
import re
s = 'aayushagrawal@gmail.com'
print(s[ : s.find("@")])
print(s[ s.find("@") : ])
