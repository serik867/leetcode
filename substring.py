e="abcabcbb"



def substring(s):

	# new_str=""
	# count=[]
	# for i in s:
	# 	if i not in new_str:
	# 		new_str+=i
	# 		print(new_str)
	# 		count.append(len(new_str))
	# 		print(count)
	# 	else:
	# 		new_str=''

	# return max(count)

	memory = []
	temp = ""
	for character in s:
		if character in temp:
			memory.append(temp)
			temp = temp[temp.find(character) + 1:] + character
		else:
			temp += character
	memory.append(temp)

	return max(len(item) for item in memory)

b="pwwkew"
c="bbbbb"
print(substring(e))
print(substring(b))
print(substring(c))