def second_largest(arr):
    if len(arr) < 2:
        return "second largest element not found"
    
    largest = float('-inf')
    second_largest = float('-inf')
    third_largest = float('-inf')

    for x in arr:
        if x > largest:
            third_largest= second_largest
            second_largest = largest
            largest = x

        elif x < largest and x > second_largest:
            third_largest = second_largest
            second_largest = x
            
        elif x < second_largest and x > third_largest:
             third_largest = x     

    if third_largest == float('-inf'):
            return "third largest element not possible"

        
    return third_largest

array = [35,0,-10,8,-5]
print(second_largest(array))           

