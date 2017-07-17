"""
16.Write a Program to Count the Number of Lines in a Text File
"""
num_lines = 0
with open("txt.txt",'r') as f:
	for line in f:
		num_lines +=1
print("Number of lines: ")
print(num_lines)