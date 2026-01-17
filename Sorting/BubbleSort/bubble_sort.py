arr = [11,15,8,2,-1]
n = len(arr)
for i in range(n):
    for j in range(1,n-i):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            
print(arr)
