# O(n log n) — Merge Sort

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    ans = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    ans.extend(left[i:])
    ans.extend(right[j:])

    return ans


nums = [1,3,7,2,4,9,9]
print(merge_sort(nums))