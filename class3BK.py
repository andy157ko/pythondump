

def fasterIsPrime(n): 
	if type(n) != int: return "Wrong Value" 		# checks for strings,bool, float being passed in 
	if abs(n) == 1: return False					# 1 and -1 being the edge case, return False
	if abs(n) == 2: return True						# 2 should be always True ;; using absolute value 
	if n % 2 == 0: return False

	for i in range(3, n): 
		#print(i)
		if n % i == 0: 
			return False 
	return True 


def testFasterIsPrime(): 
	print("testing the fasterIsPrime function!")
	assert(fasterIsPrime(7) == True)
	assert(fasterIsPrime(9) == False)
	assert(fasterIsPrime(101) == True) 
	assert(fasterIsPrime(2) == True)
	assert(fasterIsPrime(1) == False)
	assert(fasterIsPrime(-7) == True)
	assert(fasterIsPrime(-11) == True)
	assert(fasterIsPrime(-12) == False)
	assert(fasterIsPrime(-2) == True)
	assert(fasterIsPrime("banana") == "Wrong Value")
	assert(fasterIsPrime(3.989129481724) == "Wrong Value")
	print("fasterIsPrime is all good!")



testFasterIsPrime()


a = 10 
b = 3.5 
c = "text"
d = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))







