def fib(n):
	if n<=1:
		return n
	else:
		return (fib(n-1) + fib(n-2))

n = int(raw_input("Enter the value: "))
if n <= 0:
	print("Enter positive number: ")
else:  
	print("Fibonacci Sequence: ")
	for i in range(n):
		print fib(i)