def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

a = [3, 9, 5, 6, 7, 2, 10, 9]
k = 3
n = len(a)
k = k % n

reverse(a, 0, n - 1)
reverse(a, 0, k - 1)
reverse(a, k, n - 1)

print(a)
