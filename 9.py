import re, sys
password = input("Enter the password ")
y = list(password)
l = len(y)

if(l > 6 and l < 16 and re.search(r'[A-Z]',y) and re.search(r'[a-z]',y) and re.search(r'[0-9]',y)):
	print ("This is a valid password")
else:
	print ("Invalid password")

 