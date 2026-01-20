arr = [7,5,2,3,9,0,6,10]
n = len(arr)
temp = arr[n -1]

for i in range(n-2,-1,-1):
    arr[i+1] = arr[i]

arr[0] = temp

print(arr)