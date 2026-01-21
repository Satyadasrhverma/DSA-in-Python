arr = [2, 5, 6, 4, 7, 3]

def find_index(arr, target):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == target:
            return i
        i += 1
    return -1

a = int(input("Enter a target: "))
print(find_index(arr, a))
