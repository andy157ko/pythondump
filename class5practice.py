def isPalindrome(n):
	n = str(n)
	if (n[::-1] == n):
		return True
	else:
		return False
print(isPalindrome(1111))



# def rotateR(n,r,d):         # n = number that is going to be rotated, r = how many times it's going to be rotated , d = digit number
# #why does it keep telling me that n, r and d are not integers. 
# 	n = str(n)
# 	timesRotated = 0
# 	while timesRotated < r:
# 		n=n[1:d]+n[0]
# 		timesRotated = timesRotated + 1
# 		if r == timesRotated:
# 			break
# 	return n
# print(rotateR(1234,2,4))

# def testrotateR():
# 	assert(rotateR(1234,1,4) == 2341)
# 	assert(rotateR(1234,2,4) == 3412)

# (1234, 1) --> 2341
# (1234, 2) --> 3412
# (1234, 3) --> 4123
# (1234, 4) --> 1234 

# def rotateR(n,r):         # n = number that is going to be rotated, r = how many times it's going to be rotated , d = digit number
# #why does it keep telling me that n, r and d are not integers. 
# 	n = str(n)
# 	timesRotated = 0
	
# 	while timesRotated < r:
# 		n=n[1:len(n)]+n[0]
# 		timesRotated = timesRotated + 1
# 		if r == timesRotated:
# 			break
# 	return n
# print(rotateR(1234,3))

# def testrotateR():
# 	assert(rotateR(1234,1) == 2341)
#  	assert(rotateR(1234,2) == 3412)

# lowercasePercent(s): 

def fastestRotateR(n,r):
	n = str(n) #n is being changed into a string
	n = n[r:] + n[:r]
	return n

print(fastestRotateR(1234,3))


def lowercasePercent(s):
	lowercaseCounter = 0
	#s = str(s) 
	if s.find('%') == -1:
		lowercaseCounter = lowercaseCounter -1
	for i in range (0,s.find('%')):
		if s[i].islower() == True:
			lowercaseCounter = lowercaseCounter + 1
		else:
			lowercaseCounter = lowercaseCounter + 0 

	return lowercaseCounter

print(lowercasePercent("Hello I am Andy%"))

	# "I am a %boy who likes to go hiking"   ---> 3 
	# "% I am a boy"						   ---> 0 
	# "I am a boy who likes to go hiking"    ---> -1


# Write the function mostFrequentLetters(s), that takes a string s, and ignoring case 
# (so "A" and "a" are treated the same), returns a lowercase string containing the 
# letters of s in most frequently used order. 
# (In the event of a tie between two letters, follow alphabetic order.) So:
#    mostFrequentLetters("We Attack at Dawn!")
# returns "atwcdekn". Note that digits, punctuation, and whitespace are not letters! 
# Finally, if s does not contain any alphabetic characters, the result should be the empty string ("").

# def mostFrequentLetters(s):
# 	if s.isalpha() == False:
# 		return("")
# 	maxcount = 0
# 	maxletter = ""
# 	s = s.lower()
# 	# s = s.replace(',','')
# 	s = s.strip()
# 	for i in range()

# 	s.count(s[i])


# 	# for i in range (0,len(s)):
# 	# 	s[i].find('a')
# 	# 	if True:
# 	# 		repeatCounter = repeatCounter + 1
# 	# return repeatCounter

# print(mostFrequentLetters("hhhellooooa"))

def countLetters (s):
	s = s.lower()
	letters = 0
	maxLetters = ""
	maxrepeat = 0
	while letters < len(s):
		if maxrepeat < s.count(s[letters]):
			maxLetters = ""
			maxLetters = maxLetters + s[letters]
			maxrepeat = maxrepeat + s.count(s[letters])
		if maxrepeat == s.count(s[letters])and maxLetters > s[letters]:
			maxLetters = (s[letters])
		letters = letters + 1
	return maxLetters
print(countLetters ("lllzzz"))

def testcountLetters():
	assert(countLetters("bbbbbaaaaa")==b)
	assert(countLetters("asdlkjfasldjffff")==f)
	assert(countLetters(hellloooooo)==o)








