## 2D Lists ## 

myList = [1,2,3,4,5]
myList2D = [[1,2,3], [4,5]]

print(len(myList))
print(len(myList2D))

# Indexing 

print(myList2D[0])		# gets the 0th index list from myList2 
print(myList2D[0][2])	# gets the 2nd index element from the 0th index list in myList2D 

print(len(myList2D[0]))

print("----------------------------------")
# Looping over 2D Lists # 
myList3 = [[1,2,3],[3,4,5,6,7]]
 
for i in myList3: 
	print(i)
	for j in i: 
		print(j)

print("----------------------------------")
for i in range(0, len(myList3)): 
	print(myList3[i])
	for j in myList3[i]: 
		print(j)

myList3[1].append(8)
print(myList3)


def isPrime(n): 
	if n == 2: return True 
	if n < 2 or n % 2 == 0: return False 
	for i in range(3, n/2, 2): 
		if n % i == 0: return False 
	return True 



def isPrimeCounter(L): 
	
	return 


def hasDuplicate(L): 

	return 


