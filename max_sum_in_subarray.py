A = [2,1,5,1,3,2]
k=3
arr_len = len(A)
result = 0
temp = 0
for i in range(0,arr_len):
	if i < k:
		result = result + A[i]
	else:
		result = result + A[i] - A[i-k]
		temp = temp if temp > result  else result
print(temp)