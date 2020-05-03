A = [5,4,2]
# A = [1,2,3,4,5]
A.sort()
# print A
arr_len = len(A) - 1
# if arr_len == 1:
#     print A[0]
# if arr_len == 2:
#     print abs(A[0] - A[1])
result_sum = 0
result_sum1 = 0
# for i in range(0, arr_len):
#     # for j in range(arr_len, 1,-1):
#     # if arr_len == 2:
#     # 	result_sum +=  abs(A[0] - A[1])
#     # temp_arr_len = arr_len
#     for j in range(arr_len, i,-1):
#     # while(arr_len >= 1):
#     	print A[j] - A[i]
#     	print 2**(j - 0 -1)
#     	result_sum1 = (A[j] - A[i]) * (2**(j - i -1))
#         result_sum += (A[j] - A[i]) * (2**(j - i -1))
#         # temp_arr_len = temp_arr_len - 1
#     # arr_len = arr_len -1
# print result_sum
A = [1,2]
arr_len = len(A)
result_sum1 = 0
for i in range(0, arr_len):
	result_sum1 += (A[i] * (2**i - 2**(arr_len-i-1)))
	# print A[i]
	# print i
	# print arr_len-i-1
# print result_sum
print result_sum1