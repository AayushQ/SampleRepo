def Computehcf(x,y):
	if x > y:
		smaller = y
	else:
		smaller = x
	for i in range(1,smaller+1):
		if((x%i==0) and (y%i==0)):
			hcf = i
		return hcf

n1=int(raw_input())
n2=int(raw_input())

print("The hcf of ",n1, " and ",n2, ": ", Computehcf(n1,n2))
