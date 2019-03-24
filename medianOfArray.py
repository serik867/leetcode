def medianOfArray(num1,num2):

	num3 = list(set(sorted(num1+num2)))
	print(num3)
	result = 0
	
	if len(num3)%2 == 0:
		result = (num3[int(len(num3)/2)]+num3[int(len(num3)/2)-1])/2
		
		return result
	else:
		print("else")
		result = num3[len(num3)//2]

		return result


s1=[1,3]
s2=[2]

s3=[1,2,3]
s4=[4,5,6]

print(medianOfArray(s1,s2))
print(medianOfArray(s3,s4))
print(medianOfArray(s2,s4))
print(medianOfArray(s2,s3))
print(medianOfArray(s1,s4))
