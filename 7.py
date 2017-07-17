"""
7.Write a program to display an user-defined Exception
"""
class MyError(Exception):
	def __init__(self,value):
		self.value = value

	def __str__(self):
		return(repr(self.value))

try:
	raise(MyError(3*4))

except MyError as error:
	print('New Exception occurred: ',error.value)