#making a calculator
import logging

f = 1
while(f!=0):
	if f==0:
		break
	else:
		print("select the choice of calculation: ")
		print("1. Addition")
		print("2. Substraction")
		print("3. Muliplication")
		print("4. Divison")
		print("5. Exit")
		n = int(raw_input())
		if n==5:
			break
		n1 = float(raw_input("Enter the first number "))
		n2 = float(raw_input("Enter the second number "))	
		if n == 1:
                        logging.info('Add the two numbers')
			print("The sum of two number is: ", n1 + n2)
		elif n == 2:
                        logging.info('subtract the two numbers')
			print("The difference of two number is: ", n1 - n2)
		elif n == 3:
			print("The product of two number is: ", n1*n2)
		elif n == 4:
                        try:
                                if n2==0:
                                        raise ValueError("The denominator is zero")
                        except ValueError as ve:
                                print(ve)
                        print("The division of two number is: ", n1/n2)
		else:
			f=0
