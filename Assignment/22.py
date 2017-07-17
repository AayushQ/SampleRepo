"""
22.Write a program that accepts a sentence and calculate the number of letters and digits.
"""
str = input("Enter the sentence:")
l=0
d=0
for i in str:
	if i.isdigit():
		d = d+1
	
	elif i.isalpha():
		l = l+1

	else:
		pass
print("Letters",l)
print("Digits",d) 