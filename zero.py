A = [[1, 0, 1],
	[1, 1, 1],
	[1, 1, 1]]
row_len = len(A)
col_len = len(A[0])
print(row_len)
print(col_len)
row_loc = [0]*row_len
col_loc = [0]*col_len
for i in range(0,row_len):
    for j in range(0,col_len):
        if A[i][j] == 0:
            row_loc[i] = 1
            col_loc[j] = 1
for i in range(0,row_len):
    for j in range(0,col_len):
        if(row_loc[i] == 1 or col_loc[j] == 1):
            A[i][j] = 0
print(A)
