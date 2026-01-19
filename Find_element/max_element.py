def max_ele(arr):
    maximum = arr[0]

    for i in range(1,len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum
        
        
a = [3,4,6,7,22,13,1,14]
print(max_ele(a))

