# Printing the pattern of 'D'
result_str = " "
for row in range(0,7):
	for column in range(0,5):
		if((row == 0 and column != 4) or (row == 6 and column != 4) or (column == 0) or (column == 4 and (row != 0 and row != 6))):
			result_str = result_str + "* "
 		else:
			result_str = result_str + "  "
	result_str = result_str + "\n"
print(result_str)
