A = [1, 2, 2, 3, 1]
arr_len = len(A)
single_number = A[0] ^ A[1]
for i in range(2,arr_len):
	single_number = single_number ^ A[i]
print(single_number)
