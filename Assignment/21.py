"""
21.Write a Program to Read the Contents of a File in Reverse Order
"""
for line in reversed(list(open('txt.txt'))):
	print(line.rstrip())