# A = "AAAAA"[::-1]
# str_len = len(A)
# count = 0
# for i in range(str_len-1,-2,-1):
# 	if A[i] == A[+1]:
# 		continue
# 	else:
# 		count += 1

A = "HIRED" 
B = "HHHIIIRRRRREEEEEDDDDD"
B = "HHHHIIIIRRRRREEEEDDD"
import itertools
B = ''.join(ch for ch, _ in itertools.groupby(B))
print B

count = 0
str_len = len(A)
for i in range(0, str_len):
	if A[i] != B[i]:
		print 0
		break
print 1
# print count
