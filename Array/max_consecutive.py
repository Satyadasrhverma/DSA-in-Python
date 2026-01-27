arr = [1,3,4,1,2,5,6,7,1,8,1,9]

freq = {}

for i in arr:
    freq[i] = freq.get(i,0) + 1

    if freq[i] == 2:
        print(i)

#################################
arr = [1,3,4,1,2,5,6,7,1,8,1,9]

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1

for k, v in freq.items():
    if v >= 2:
        print(k)
