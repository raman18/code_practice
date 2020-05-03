A = [4, 5, 2, 10, 8]
arr_len = len(A)
stack = []
result = []
for i in range(arr_len):
	while len(stack) and stack[-1] >= A[i]:
		stack.pop()
	if not len(stack):
		result.append(-1)
		stack.append(A[i])
	else:
		result.append(stack[-1])
	stack.append(A[i])
print result