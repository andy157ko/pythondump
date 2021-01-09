# def alternatingSum(L): 
# 	placeValue = 0
# 	theSum = 0
# 	while placeValue < len(L):

# 		if placeValue % 2 ==0:
# 			theSum = theSum + L[placeValue]
# 		else:
# 			theSum = theSum -L[placeValue]
# 		placeValue = placeValue + 1
#  	return theSum
# print(alternatingSum([5,4,3]))

# def anotherAlternatingSum(L):
# 	answer = 0
# 	for i in range(0,len(L)):
# 		if i % 2 == 0:
# 			answer = answer + L[i]
# 		else:
# 			answer= answer - L[i]
# 	return answer 

# print(anotherAlternatingSum([5,4,3]))

# def lastAlternatingSum(L):
# 	return sum(L[::2]) - sum(L[1::2])
# print(lastAlternatingSum([5,4,3]))

def median(L):
	median = 0
	L.sort()
	if len(L)%2==0:
		median=(L[len(L)/2]+L[len(L)/2-1])/2.0
	else:
		median=L[len(L)/2]
	return median

print(median([6,5,4,3,2,1]))

def testmedian():
	assert(median([5,3,4,7,6])==5)

def mode(L):
	numbers = 0
	maxrepeat = 0
	mode = 0
	while numbers < len(L):
		if maxrepeat < L.count(L[numbers]):
			mode = L[numbers]
			maxrepeat = L.count(L[numbers])
		if maxrepeat == L.count(L[numbers]) and mode > L[numbers]:
			mode = (L[numbers])
		numbers = numbers + 1
	return mode
print(mode([1,2,2,2,3,3,3]))

def testmode(L):
	assert(mode([1,5,6,2,3,1]==1))
	assert(mode([1,1,1,2,2,2,3,3,3]==1))

def average(L):
	return sum(L)/len(L)
print(average([2,2,2]))




