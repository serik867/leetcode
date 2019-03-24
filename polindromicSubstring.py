def polindromicSubstring(s):
	def checkPol(str1):
		if str1 == str1[::-1]:
			return True


	list1=[]

	substr=""
	for i in s:
		substr+=i
		
		if checkPol(substr):
			list1.append(substr)
	for i in s:
		substr=s
		if checkPol(substr.translate(table[None, i])):
			list1.append(substr)


s="ababcd"
s1="babad"

polindromicSubstring(s1)