def second_max(arr):
    if len(arr) < 2:
        return "not possible"

    largest = float('-inf')
    second = float('-inf')

    for x in arr:
        if x > largest:
            second = largest
            largest = x
        elif x < largest and x > second:
            second = x

    if second == float('-inf'):
        return "not possible"

    return second


a = [3, 4, 5, 67, 2]
print(second_max(a))
