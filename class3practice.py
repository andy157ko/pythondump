def fasterIsPrime(n):
	if type(n) != int:
		return "Please enter an integer!"
	if abs(n) == 1:
		return False
	if abs(n) == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range (3, n /2):
		if n % i == 0:
			return False
	return True

def TestfasterIsPrime():
	print("Starting test on fasterIsPrime")
	assert(fasterIsPrime(1) == False)
	assert(fasterIsPrime("haha") == "Please enter an integer")
	assert(fasterIsPrime(171)== True)
	print("fasterIsPrime works")

# 1234, 4 digits, for loops, divide the digits

print("--------------")

def sumOfDigits(n, d):
 	if type(n) and type(d) != int:
 		return "Please enter an integer"
	theSum = 0
	if n < 0:
		for i in range (0, d):
			digit = abs(n) % 10
			theSum = theSum + digit
			n = abs(n) / 10
		return theSum * -1


	for i in range (0, d):
		digit = n % 10
		theSum = theSum + digit
		n = n / 10
	return theSum 


print(sumOfDigits(-10293284374,11))

def testsumOfDigits():
	print("testing the sum of digits")
	assert(sumOfDigits(16789,5) == 31)
	assert(sumOfDigits(yo,5) == "Please enter an integer")
	assert(sumOfDigits(1,1) == 1)
	assert(sumOfDigits(-12,2) == -3)






