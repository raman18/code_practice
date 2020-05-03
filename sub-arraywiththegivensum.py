A = [ 42, 9, 38, 36, 48, 33, 36, 50, 38, 8, 13, 37, 33, 38, 17, 25, 50, 50, 41, 29, 34, 18, 16, 6, 49, 16, 21, 29, 41, 7, 37, 14, 5, 30, 35, 26, 38, 35, 9, 36, 34, 39, 9, 4, 41, 40, 3, 50, 27, 17, 14, 5, 31, 42, 5, 39, 38, 38, 47, 24, 41, 5, 50, 9, 29, 14, 19, 27, 6, 23, 17, 1, 22, 38, 35, 6, 35, 41, 34, 21, 30, 45, 48, 45, 37 ]
B = 100
arr_len = len(A) - 1
result_arr = []
result_arr = [A[0]]
result_sum = A[0]
for i in range(1, arr_len):
	result_sum += A[i]
	result_arr.append(A[i])
	print(result_sum)
	print(result_arr)
	if(result_sum == B):
		print("answer found")
		print result_arr
	elif(result_sum > B):
		while(sum(result_arr) >= B):
			k = 0
			result_sum -= result_arr[k]
			result_arr.pop(k)
			if(sum(result_arr) == B):
				print("answer found insisw while loop")
				print(result_arr)
				break
			k += 1
	elif(result_sum < B):
		continue
print [-1]
https://www.geeksforgeeks.org/find-a-triplet-in-an-array-whose-sum-is-closest-to-a-given-number/