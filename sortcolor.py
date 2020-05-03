n = 7
a = [1,2,1,0,1,0,2]
for i in range(0,n,1):
    for j in range(0,n-1,1):
        if(a[j] > a[j+1]):
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp;
print(a)
