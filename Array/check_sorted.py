def is_sorted(arr):
    if len(arr) < 2:
        return False
    
    i = 0
    while i < len(arr) -1 :
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True    


a = [2,3,4,5,6]
print(is_sorted(a))