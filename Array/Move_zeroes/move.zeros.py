def move_zero(arr):
    n = len(arr)
    if n <= 1:
        return arr

    i = 0

    # find first zero
    while i < n:
        if arr[i] == 0:
            break
        i += 1

    if i == n:
        return arr   # no zero found

    j = i + 1

    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    return arr
array = [2,4,5,6,0,2,3,0,5,6,0]
print(move_zero(array))
