A = [1,3,9]
arr_len = len(A)
if(arr_len == 1):
    return A[0]
max_gcd = A[0]
for i in range(0, arr_len):
    X = max_gcd
    Y = A[i]
    while(X): 
        Y, X = X, Y % X
        max_gcd = Y
return max_gcd