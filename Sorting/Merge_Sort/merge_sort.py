def merge(arr1,arr2):

    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0

    result = []


    while i < m and j < n:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < m:
        result.append(arr1[i])
        i += 1

    while j< n:
        result.append(arr2[j])            
        j += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_a = merge_sort(left)
    right_b = merge_sort(right)

    return merge(left_a , right_b)

b = [3,6,3,-1,0,4]
print(merge_sort(b))    