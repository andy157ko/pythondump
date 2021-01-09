# data types 

# integer 
# 0, 30, -99 

# float (decimal)
# 0.4, -9.0, 17.3344444

# string (text)
# "Andrew", "Andy", "30"

# Boolean (T/F)
# True, False 

# print 
print(100)
print("100")

# <--- commenting 

# Operations 
# 	+, -, *, /, %, ** 
print(3 + 3)
print("3" + "3")
print("An" + "dy")

print(10 - 7)		# subtraction
print(2 * 10)		# product
print(10 / 3)		# quotient (* in python 3 / gets the exact value)

print(10 % 3)		# remainder 
print(2 ** 3)

#  >, <, ==, ! 
print(10 > 3)
print(10 < 3)
print(10 == 10)
print(10 == "10")	 # False, because they are representing diff data type s
print(10 != 3)		 # ! means not 
print(10 >= 10)
print(10 <= 90)

# Variables 
x = 10 
y = 5
x = 9 
print(x + y)

print("----------------------------------------------")

def chocolateIceCream(chocolate): 	
# def + function name + ( ingredients ) + :
	numOfIceCream = chocolate / 10	# divide choc by 10
	print(numOfIceCream) 	# temporary output 

chocolateIceCream(12)	#calling the function with input

print("----------------------------------------------")

x = -999 
# if x > 0: 
# 	print ("Yes")
# else: 
# 	print ("NO!")

# BAD numberToGrade 
grade = 91 
if grade > 90: 
	print("A")
if grade > 80: 		# still runs this case 
	print("B")
if grade > 70: 		# still runs this case 
	print("C")
else: 
	print("F")

print("----------------------------------------------")

# Bad numberToLetterGrade 2
grade = 91 
if grade > 90: 	
	print("A")
if 89 > grade > 80: 		# doesn't apply 
	print("B")
if 79 > grade > 70: 		# doesn't apply 
	print("C")
else: 						# still prints F because 91 is not a C 
	print("F")

print("----------------------------------------------")

# Good numberToLetterGrade 

grade = 91 
if grade > 90: 	
	print("A")
elif grade > 80: 		# doesn't apply 
	print("B")
elif grade > 70: 		# doesn't apply 
	print("C")
else: 					# doesn't apply  
	print("F")








