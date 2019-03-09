def iseven(n):
	return(not(n & 1))
n=10;
print("even" if iseven(n) else "odd" )