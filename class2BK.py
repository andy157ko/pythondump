def isMultiple(m,n): 
	if n == 0: 
		print(False)
	else: 
		remainder = m % n 
		if remainder != 0: 
			print(False)
		else: 
			print(True)

#isMultiple(10,0) 		# True
#isMultiple(10,6)		# False 

# isLegalTriangle(s1, s2, s3) 

#print(10 > 3 + 10)

def isLegalTriangle(s1, s2, s3): 
	# if s1 is the longest side 
	if s1 > s2 and s1 > s3: 
		print(s1 < s2 + s3)
	# if s2 is the longest side 
	elif s2 > s3: 
		print(s2 < s1 + s3)
	# if s3 is the longest side 
	else: 
		print(s3 < s2 + s1)

#isLegalTriangle(30, 31, 13)

# print(10, 3, 4)
# print(max(10, 3, 4))		# maximum value	
# print(min(10, 4, 4))		# minimum value 
x = -10 
# print(abs(x))				# absolute value 


def fasterIsLegalTriangle(s1, s2, s3): 
	maxSide = max(s1, s2, s3)
	perimeter = s1 + s2 + s3 
	print(maxSide < perimeter - maxSide) # sum of two shorter sides 

#fasterIsLegalTriangle(10, 3, 9)


# print vs. return 

# return statement ends the function 
# print statement simply prints the value for you to see. 
# 	Doesn't save or pass the value to the next function (no output!)... returns NONE 


def isOdd(n):
	print(1)
	if n % 2 == 1: 
		# print(True)			
		# print("checkpoint 2")			# for debugging purposes 
		print(2)
		return True
		print(3)
	else: 
		# print(False)
		# print("checkpoint 3")			# not supposed to print checkpoint 3
		print(4)
		return False 
	print(5)

# return statement simply ends the function 
# isOdd(7)			# prints 1, 2 
# isOdd(8)			# prints 1, 4

def multiplyBy10(n): 
	# print(isOdd(n))		# None if we use the print statement in isOdd

	if isOdd(n) == True:				# calling isOdd function written above; checking if n is odd 
		# print("checkpoint 1") 
		return n * 10					# returns n * 10 if odd 
	else: 
		return n 						# if n is not an odd number, just returns n 

#print(multiplyBy10(7)) 


for loop 

for i in range(1, 101):  		# 100 is not included... UPTO 99
	print(i)					# i is generally used as an index value in a forloop 
								the 'i' can be replaced with other variable names such as number 
	
for i in range(1, 101): 
	if i % 5 == 0: 
		print(i)

for i in range(1, 101, 2): 		# 2 represents increment (increasing by)
								by default this is 1 
	print(i)


for i in range(100, -1, -1): 	# reversing the for loop 
	print(i)
