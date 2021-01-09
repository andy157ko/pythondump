def eggCarten(eggs):

	numofCartens = eggs / 12

	if eggs % 12 != 0:
		print(numofCartens + 1)
	else:
		print(numofCartens)

eggCarten(13)


print("--------------------------")

def fabricYards(inches):

	yardsofFabric = inches / 36

	if inches % 36 != 0:
		print(yardsofFabric +1)
	else:
		print(yardsofFabric)
fabricYards(5)

print("--------------------------")

def fabricExcess(inches) :

	amountofFabric = inches 

	if inches % 36 != 0:
		print(amountofFabric % 36)
	else:
		print("0")
fabricExcess(38)

print("-------------------------")

def isMultiple(m,n):

	
	
	if n == 0:
		print("False")
	else:
		multiple = m % n
		if multiple != 0:
			print("false")
		else:
			print("true")


isMultiple(11,11)


print("----------------------------")

def currencyExchange(won):

	dollars = won // 1109

	if dollars > 0:
		print(dollars)

	else:
		print("0")

currencyExchange(500)

print("------------------------------")

def isLegalTriangle(s1,s2,s3):

	a = max(s1,s2,s3)
	b = min(s1,s2,s3)
	c = s1+s2+s3-(a+b)

	print(a<b+c)

isLegalTriangle(220,21,221)

print("---------------------------")

def isRightTriangle(x1,x2,x3):

	perimeter = x1 + x2 + x3
	hypotenuse = max(x1,x2,x3)
	smallestSide = min(x1,x2,x3)
	lastSide = perimeter - max - min
	print(hypotenuse**2==smallestSide**2+lastSide**2)

isRightTriangle(220,21,221)












