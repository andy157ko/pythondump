def isPrime(n): 
	if n == 2: return True 
	if n < 2 or n % 2 == 0: return False 
	for i in range(3, n/2, 2): 
		if n % i == 0: return False 
	return True 



def isPrimeCounter(L):
	primeCount = 0 
	for i in L: 
		for j in i: 
			if isPrime(j) == True:
				primeCount = primeCount + 1
	return primeCount
print(isPrimeCounter([[1,2,3], [2,4,5]])) 
 
#similar logic
#use count find a way to count the 2D list
#transform the list
#take out similar numbers

def hasDuplicate(L): 
	duplicateCount = 0
	placeNumber1 = 0 
	placeNumber2 = 0
	for i in L:
		for j in i:
			if L[placeNumber1][placeNumber2]%L[j] == 0:
				duplicateCount = duplicateCount + 1
			if placeNumber1 == len(L[placeNumber1]):
				placeNumber2 = placeNumber2 + 1



print(hasDuplicate([[1,2,3], [2,4,5]]))





