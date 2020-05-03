from collections import deque 
A = [1,3,-1,-3,5,3,6,7]
B = 3 
stack = deque()
result_array = []
arr_len = len(A)
maximum = A[0]
for i in range(B): 
	stack.append(A[i]);
result_array.append(max(stack))
i = 1
for j in range(B,arr_len):
	stack.popleft()
	stack.append(A[j])
	result_array.append(max(stack))
	i += 1

print stack
print result_array