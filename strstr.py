A = "lll"
B = "heflllo"
A = "b"
B = "baba"
B = "aabaaaababaabbbabbabbbaabababaaaaaababaaabbabbabbabbaaaabbbbbbaabbabbbbbabababbaaabbaabbbababbb"
A = "bba"   
B = "b"
A = "b"            
str_len_A = len(A)
str_len_B = len(B)
j = 0
i = 0
if str_len_A > str_len_B:
    print -1
while j < str_len_B:
	if A[i] != B[j]:
		j += 1
		continue
	elif A[i] == B[j]:
		ci = i
		cj = j
		while ci < str_len_A and cj < str_len_B and A[ci]==B[cj]:
			ci+=1
			cj+=1
		if ci == str_len_A:
			print j
			# j = str_len_B
			break
		else:
			j += 1
# print -1
# while j < str_len_B:
# 	if A[i] != B[j]:
# 		if i > 1:
# 			j -= 1
# 		if i == 0:
# 			j += 1
# 		else:
# 			i = 0
# 	elif A[i] == B[j]:
# 		i += 1
# 		if i == str_len_A:
# 			print j + 1 - i
# 			break
# 		j += 1
print -1