A = 3
result_arr 	= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cur_row = 0
cur_col = 0
arr_val = 1
for arr_len in range(0,3):
	if arr_len == 0 or arr_len % 2 == 0:
		for col in range(cur_col,4-arr_len):
			result_arr[cur_row][col] = arr_val
			arr_val = arr_val + 1
		cur_row = arr_len + 1
		cur_col = col
		for row in range(cur_row,4-arr_len):
			result_arr[row][col] = arr_val
			arr_val =  arr_val + 1
		cur_row = row
	elif arr_len % 2 == 1:
		for col2 in range(cur_col,0,-1):
			result_arr[cur_row][col2-1] = arr_val
			arr_val = arr_val + 1
		cur_col = col2-1
		for row in range(cur_row,1,-1):
			result_arr[row-1][cur_col] = arr_val
			print(row-1)
			print(cur_col)
			print(arr_val)
			arr_val = arr_val + 1
		cur_row = row-1
		cur_col = cur_col+1
	print(result_arr)