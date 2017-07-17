"""
25.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
"""
def createDict(n):
	dictofnumb = dict()
	for i in range(n):
		dictofnumb[i]=i*i
	return dictofnumb

print(createDict(10))
