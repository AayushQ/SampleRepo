"""
23.Write a Program to Read a String from the User and Append it into a File
"""
s = input("Enter the string: ")
f =  open('txt.txt',"a")
f.write("\n")
f.write(s)
f.close()
