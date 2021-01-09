def isPrime(n):

	for i in range (2,n/2):
		print(i)
		if n % i == 0:
			return False
	return True

print(isPrime())



	

