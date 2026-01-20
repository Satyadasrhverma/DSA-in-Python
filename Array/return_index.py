
arr =[2,5,6,4,7,3]

def find(value):
    a = False
    target  = value
    for i in range(0,len(arr)):
        if arr[i] == target:
            a = True
            print(i)
    if a == False:
        print("there is not such value")

value = int(input("enter the value whose index you want "))
find(value)