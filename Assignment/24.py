"""
24.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
"""
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)