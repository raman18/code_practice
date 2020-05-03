A = 4
power   = 1
answer  = 0
power   = 1
result  = 0
while(A):
	power = power * 5
	if(A & 1):
		print("count me")
		result += power
	A >>= 1
print(result)
# while(A):
# 	temp_var1 = (temp_var1 * 5)
# 	i = i + 1
# 	print(temp_var1)
# 	if(i == A):
# 		print("1 is answer")
# 		print(temp_var1)
# 	temp_var2 = temp_var1 + 5
# 	print(temp_var2)
# 	i = i + 1
# 	if(i == A):
# 		print("2 is answer")
# 		print(temp_var2)

