# def sumOfDegits(n,d):
# 	if type(n) != int and type(d) != int:
# 		return("Please enter an integer")
# 	addedValue = 0
# 	if n < 0:
# 		for i in range (0,d):
# 			#print(i)
# 			digitValue = abs(n) % 10
# 			addedValue = addedValue + digitValue
# 			n = abs(n)/10
# 		return addedValue * -1

# 	for i in range (0,d):
# 		digitValue = n % 10
# 		addedValue = addedValue + digitValue
# 		n = n/10
# 	return addedValue

# print(sumOfDegits(-132,3))

# def testsumOfDigits():
# 	assert(sumOfDigts(-1111,4) == -4)

# def sumOfDigits(n):
# 	addedValue = 0
# 	if type(n) != int:
# 		return("Please enter integer")
# 	if n<0:
# 		while n < 0:
# 			digitValue = abs(n) % 10
# 			addedValue = addedValue + digitValue
# 			n = abs(n)/10
# 		return addedValue * -1
# 	while n > 0:
# 		digitValue = n % 10
# 		addedValue = addedValue + digitValue
# 		n = n/10
# 	return addedValue

# print(sumOfDigits(1234))

# print("testing sum of digits")
# def testsumOfDigits():
# 	assert(sumOfDigits(111111) == 6)
# 	assert(sumOfDighits(-11) == -2)
# 	assert(sumOfDigits("abc") == "Please enter integer")
# print("Sum of digits works fine")
# n = nth of Prime

# n=1 then ans =2
# n=2 then ans =3
# n=3 then ans =5


# def fasterIsPrime(n):   #do not touch    #Cheching if n is prime

# 	if type(n) != int:
# 		return "Please enter an integer!"
# 	if abs(n) == 1:
# 		return False
# 	if abs(n) == 2:
# 		return True
# 	if n % 2 == 0:
# 		return False
# 	for i in range (3, n /2):
# 		if n % i == 0:
# 			return False
# 	return True

# def nthTrue(n):							#Giving out the nth Prime
# 	primeCounter = 0
# 	number = 2
# 	while primeCounter < n:
# 		if fasterIsPrime(number) == True:
# 			primeCounter = primeCounter + 1
# 		if primeCounter == n:
# 			break
# 		number = number + 1
# 	return number



def fasterIsPrime(a):   #do not touch    #Cheching if n is prime

	if type(a) != int:
		return "Please enter an integer!"
	if abs(a) == 1:
		return False
	if abs(a) == 2:
		return True
	if a % 2 == 0:
		return False
	for i in range (3, a /2):
		if a % i == 0:
			return False
	return True

def nthPrime(n):
	if type(n) != int:
		return "Please enter an integer!"
	primeCounter = 0
	number = 2 

	while primeCounter < n:
		if fasterIsPrime(number) == True:
			primeCounter = primeCounter + 1
		if primeCounter == n:
			break
		number = number + 1
	return number
print("a")
print(nthPrime("alp"))
print("b")
def testnthPrime():
	assert(nthPrime(11)==5)


n =1234
n = str(n)
print(n[1])
















































