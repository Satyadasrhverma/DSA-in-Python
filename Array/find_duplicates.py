arr = [1,3,4,5]
s = 0
t = 0
n = len(arr)
for i in arr:
    s = s + i
for j in range(1,6):
    t +=j

print(t-s)