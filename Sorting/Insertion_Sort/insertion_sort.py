arr = [5,3,6,2,7,8,22]

size = len(arr)

for i in range(1,size):
    index = i

    while index > 0 and arr[index] < arr[index -1]:
        arr[index], arr[index -1] = arr[index-1], arr[index]

        index -=1


print(arr)            