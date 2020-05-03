A = [0, 4, 7, 9]
A.sort()
arr_len = len(A)
temp = A[0] ^ A[1]
for i in range(0,arr_len-1):
	temp = temp if temp < A[i] ^ A[i+1] else A[i] ^ A[i+1]
print(temp)


