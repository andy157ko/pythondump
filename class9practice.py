# def leastLetters(s):
# 	leastRepeat = len(s)
# 	leastRepeated = ""
# 	answer = ""
# 	while 0 < len(s):
# 		for i in range (0,len(s)):
# 			if leastRepeat > s.count(s[i]):
# 				leastRepeat = s.count(s[i])
# 				leastRepeated = s[i]
# 			elif leastRepeat == s.count(s[i]) and leastRepeated < s[i]:
# 				leastRepeated = s[i] 
# 		s = s.replace(leastRepeated,"")
# 		leastRepeat = len(s)
# 		answer = answer + leastRepeated
# 	return answer
# print(leastLetters("eeeeeaabbcc"))












def leastLetters(s):
	answer = ""
	leastRepeat = len(s) + 1
	leastRepeated = ""
	while 0 < len(s):
		for i in range(0,len(s)):
			if leastRepeat > s.count(s[i]):
				leastRepeat = s.count(s[i])
				leastRepeated = s[i]
			elif leastRepeat == s.count(s[i]) and leastRepeated > s[i]:
				leastRepeated = s[i]
		s = s.replace(leastRepeated,"")
		leastRepeat = len(s) + 1 
		answer = answer + leastRepeated
		leastRepeated = ""
	return answer
print(leastLetters("eeeeaabbcc"))
























