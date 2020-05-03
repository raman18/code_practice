A = 100
B = [20, 20, 20, 20, 5, 5, 10]
i = 0
while A != 0:
	A = A - min(A,B[i])
	if(A == 0):
		print(i+1)
		break
	i += 1
	if(i == 7):
		i = 0
