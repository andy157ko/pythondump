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


def nthPrime(n):
	primeCounter = 0 		# counts prime numbers 
	number = 2 
	while primeCounter < n:
		if fasterIsPrime(number) == True: 		# checks if the number is a prime number 
			primeCounter = primeCounter + 1 
		if primeCounter == n: 
			break 								# leaves the loop. Prevents adding 1 before returning the number 
		number = number + 1 					# number has to increase every iteration 

	return number 

#print(nthPrime(5))


#########################################################################################
## Strings ## 

# typecasting 
x = 1234 
print(type(x))			# integer currently 
print(str(x))			# convert x into string "1234" ** only in this instance 
str(x)					# this wouldn't convert it to string and store it 
x = str(x)
# x = x + 1			# same logic  
print(type(x))		# now x is converted to string

# finding the length of string 
string = "abcde"
print(len(string))		# prints 5 

# ASCII Code Table 
print(ord("a"))			# converting character to ASCII value 
print(chr(97))			# converting ASCII value to character 
print("a" > "b")		# you can compare character values 
print("a" > "A")		# a - 97 , A - 65 

# simple operations 
print("abc" + "def")	# abcdef  --> string concatenation 
print("abc" * 3)		# abcabcabc   --> printing abc 3 times 
#print("abc" + 3)		# abc3	--> Error! Str and Int cannot be added together 

# in operator 
print("ring" in "string")    # True 
print("abc" in string)		 # True 

# indexing 
string = "abcdefg"
print(string[0])		# prints the 0th (1st) index of the string ... a 
print(string[6])		# prints the 6th (7th) index of the string... g 
print(string[-1])		# prints the -1th also the last index of the string ... g 
#print(string[7]) 		# Error! 7th index doesn't exist... 		string index out of range

print(string[0:3])		# 0th index UPTO the 3rd index (3rd index is excluded)    # abc
print(string[1:3])
print(string[1:])		# 1st index to ~ ... if it's blank it goes till the end 
print(string[:4])		# from the beginning UPTO the 4th index 
print(string[1:6:2])	# from 1st UPTO 6th index INCREMENTS by 2 
print(string[:])		# prints everything
print(string[::-1])		# reverse! traversing from the end to the beginning (-1)


# loop through the string 
sentence = "I am a boy"

for i in range(0, len(sentence)): 		# looping through sentence with index 
	print(i, sentence[i])
	# print(sentence[i])
	# if i % 2 == 1: 
	# 	print(sentence[i])

for character in sentence: 			# does the same thing... without the index! 
	print(character)				# can only be used to loop every character... limited without index in the for loop 


# split # 
names = "Andrew,Andy,David"	
for name in names.split(","): 		# takes the ',' erases it and replaces by a new line
	print(name)

# Strings are immutable 
s = 'abcde'
print(s[2])
# s[2] = 'z'						 # str does not support item assignment
s = s[:2] + "z" + s[3:]
print(s)							 # the new string with c replaced by z 



# Basic String Methods  

s1 = "abcde"
s2 = "ABCDE"
s3 = "12345"
s4 = "abCde"

# checking 
print(s1.islower())			# checks if s1 is all lowercase
print(s4[0:3].islower())			# even if only 1 uppercase exists, still prints False 
print(s2.isupper())
print(s3.isdigit())			# checks if all char are digits 
print(s1.isalpha()) 		# checking if all chars are alphabets 

# converting 
print(s1.upper())			# changes to uppercase. BUT ONLY IN THIS INSTANCE 
s1 = s1.upper()
print(s1)
print(s2.lower())


s5 = "               b o  o             "
print(s5)
print(s5.strip())			# strip all the empty trailing spaces only (NOT SPACES BETWEEN CHARs)

# replace 
print(s2.replace('C', 'Z'))		# replaces the 'C' with the 'Z'

# counting and finding indexes 
s6 = "I lik to at cookis"
print(s6.count('e'))			# counts the letter 'e' in sentence s6 
print(s6.find('e'))				# finds the FIRST occurrence of e and returns the index of that character 



############## EXCERCISES ################### 
def isPalindrome(n): 
	return 

# 123454321 --> True 
# 1 --> True 
# 8919  --> False 
# will be passed in an integer n 

def rotateR(n,r): 

	return 

# (1234, 1) --> 2341
# (1234, 4) --> 1234 
# will be passed in an integer n and r. 
# r is the number of times you have to rotate digits in n to the left 











