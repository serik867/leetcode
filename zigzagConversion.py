def zigZagConversion(_str,numRows):
	if numRows == 1 or numRows >= len(s):
		return s
		
	L = [''] * numRows
	index, step = 0, 1

	for x in _str:
		L[index] += x

		if index == 0:
			step = 1
		elif index == numRows -1:
			step = -1
		index += step

	return ''.join(L)


s= 'PAYPALISHIRING'
t= "SERDARDUR"

print(zigZagConversion(s,4))
print(zigZagConversion(t,3))

