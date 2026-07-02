 # Logarithmic Time or Binary Search

def binary_search(nums, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(mid)
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
arr = list(range(101))
target = 76
print(arr)
binary_search(arr, target)

