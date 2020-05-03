A = 10
prime = [True for i in range(A+1)] 
p = 2
result_array = []
while (p * p <= A): 
    if (prime[p] == True): 
        for i in range(p * p, A+1, p): 
            prime[i] = False
    p += 1
arr_len = len(prime)
for i in range(2,arr_len):
    if prime[i] == True:
        result_array.append(i)
arr_len = len(result_array)
i = 0
j = arr_len -1
while i < arr_len:
    if result_array[i] + result_array[j] == A:
        # print [result_array[i],result_array[j]]
        print result_array[i]
        print result_array[j]
        break
    elif result_array[i] + result_array[j] > A:
        j -= 1
    elif result_array[i] + result_array[j] < A:
        i += 1
# return -1