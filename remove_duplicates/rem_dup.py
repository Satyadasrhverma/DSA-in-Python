arr = [3,3,4,56,66,6,7,9,8,8]

result = []

for x in arr:
    if x not in result:
        result.append(x)

print(result)        
