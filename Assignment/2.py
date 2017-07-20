""" 2.Write a program to demonstrate printing pattern of alphabets

A 
B C 
D E F 
G H I J 
K L M N O 
"""
num = 65
for i in range(0,5):
	for j in range(0,i+1):
		ch = chr(num)
		print(ch) ,
		num = num +1
	print("\r")