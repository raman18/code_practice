A = "123"
str_len = len(A)
temp_str = ""
temp_arr = []
for i in range(0,str_len):
	if A[i] == "1":
		temp_str += "1"
	if A[i] == "2":
		temp_str += "abc"
	if A[i] == "3":
		temp_str += "def"
print(len(temp_str))
print(temp_str)
for i in range(0, len(temp_str)):
	for j in range(i,len(temp_str)-1):
		print(j)
		temp_arr.append(A[i] + A[j])

print(temp_arr)
# for 