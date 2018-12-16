def fibonacci(n,k):
	if(n == 1):
		return 1
	elif(n ==2):
		return k

	one = fibonacci(n - 1, k)
	two = fibonacci(n - 2, k)

	if(n <=4):
		return (one + two)

	return (one+ (two*k))

print fibonacci(33,3)
