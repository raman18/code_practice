A = [ 3, 6, 3, 1, 6 ]
target = 18
arr_len = len(A)
result = 0
temp = 0
result_length = arr_len+1
temp_length = 0
temp_val = 0
for i in range(0,arr_len):
	temp_val = temp_val + A[i]
	temp_length = temp_length + 1
	while temp_val >= target:
		result_length = temp_length if temp_length < result_length else result_length
		temp_val = temp_val - A[i+1 - temp_length]
		temp_length = temp_length -1
		
print(result_length)

