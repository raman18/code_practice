A = [5, 17, -22, 11]
A = [ -78, -97, -44, -18, -7, -26, 37, -76, -23, -35, 48, 9, 25, 62, -90, 27, -40, 18, 88, 82, 15, 96, 31, -2, -45, -48, 52, -78, -79, -76, -18, -88, -85, 58, -48, -48, -16, 77, -79, -89, -78, 27, 98, 53, -6, 43, 73, 38 ]

hashmap = {}
arr_len = len(A) - 1
prefix_sum = A[0]
result_index = 0
for i in range(0,arr_len):
	prefix_sum += A[i]
	if(prefix_sum in hashmap):
		print 1
		# result_index = i - hashmap[A[i]]
	else:
		hashmap[A[i]] = i
if(result_index == 0 ):
	print 0
else:
	print 1