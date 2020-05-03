a = [1,3,5,6]
t = 100
for i in range(0,len(a),1):
	if(a[i] == t):
		print(i)
		break
	elif(a[i] > t and i >0):
		print(i)
		break
	elif(a[i] > t and i == 0):
		print(i)
		break
	elif(i+1 == len(a)):
		print(i+1)
		break



