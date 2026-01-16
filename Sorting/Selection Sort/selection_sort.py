arr = [2,3,1,0,6,5]

for i in range(len(arr)):
    index = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[index]:
            index = j 

            arr[i], arr[index]= arr[index] , arr[i] 
print(arr)   
#this is selection sort  