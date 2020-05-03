A = "abbaba"
B = [3,5,2,4,1,1]
C = "ab"
str_len = len(A)
print(str_len)
seq_len = len(C)
hashmap = {}
for i in range(0,str_len):
	if A[i] in hashmap.keys(): 
	    if(hashmap[A[i]] > B[i]):
	    	hashmap[A[i]] = B[i]
	else: 
	    hashmap[A[i]] = B[i]
#for i in range(0,str_len):
print(hashmap)
#https://www.geeksforgeeks.org/count-distinct-occurrences-as-a-subsequence/