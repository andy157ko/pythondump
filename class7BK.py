def countLetters (s):
	s = s.lower()
	letters = 0
	maxLetters = ""
	maxrepeat = 0
	while letters < len(s):
		if maxrepeat < s.count(s[letters]):
			maxLetters = s[letters]
			maxrepeat = s.count(s[letters])
		if maxrepeat == s.count(s[letters]) and maxLetters > s[letters]:
			maxLetters = (s[letters])
		letters = letters + 1
	return maxLetters


print(countLetters ("zhhhoollooe"))



def testcountLetters():
	assert(countLetters("bbbbbaaaaa")==b)
	assert(countLetters("asdlkjfasldjffff")==f)
	assert(countLetters(hellloooooo)==o)


### Lists ### 

a = [1,2,3,4,5,'apple','pear']
print(a)
print(type(a))			# list 

print(len(a))			# prints # of elements in the list 

# Indexing 

print(a[0])				# 1 
print(a[6])				# 'pear'
# print(a[7])				# IndexError: list index out of range
print(a[1:])			#[2, 3, 4, 5, 'apple', 'pear']
print(a[:6])			#[1, 2, 3, 4, 5, 'apple']
print(a[::-1])			# reverse  ['pear', 'apple', 5, 4, 3, 2, 1]

# min, max, sum 
b = [1,2,3]
print(max(b))			#3
print(min(b))			#1
print(sum(b))			#6

# strings, integers are immutable 
x = 10 
x + 10 
print(x)

x = x + 1 
print(x)

# lists are mutable 
a = [1,2,3]

# append # 
a.append(6)			# adding the element to the end of the list, [1, 2, 3, 6]
print(a)

# index 
print(a.index(3))	# returns the index number of the element 3 

# insert
a.insert(2, "pie")	# inserts the word pie into the 2nd index 
print(a)

# replacing 
a[2] = "cake"
print(a)

# remove 
a.remove("cake")	# removes the "cake" element from list a 
print(a)

# pop 
a.pop(2)			# removes the element with index number 2 
print(a)

# in 
print(1 in a) 		# returns whether 1 is in list a 

# Looping over List 
a = [1,3,6,5,2]

for i in range(0, len(a)): 
	print(a[i])

# for element in a: 
# 	print(element)

# sorting, reversing 
print(a)
a.sort()
print(a)			# sorted in an increasing order 

a.reverse() 
print(a)


def alternatingSum(L): 
# Write the function alternatingSum(L) that takes a list of numbers and 
# returns the alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). 
# If the list is empty, return 0.

	return 






