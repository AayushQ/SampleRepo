# E Pattern
result_str = ""
for row in range(0,7):
	for column in range(0,5):
		if(row == 0 or row == 6 or column == 0 or (row == 3 and (column == 1 or column == 2 or column == 3))):
			result_str = result_str + "* "
		else:
			reslut_str = result_str + "  "
	result_str = result_str + "\n"
print(result_str)
