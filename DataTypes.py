# int
# float
# str
# bool
# list
# tuple
# dict
# set

# ===================== PYTHON MUTABILITY & SLICING NOTES =====================

# MUTABLE (object can be modified)
# --------------------------------
# list       -> [1, 2, 3]
# dict       -> {"a": 1}
# set        -> {1, 2, 3}
# bytearray  -> bytearray(b"abc")

# IMMUTABLE (cannot modify the object itself)
# -------------------------------------------
# str        -> "hello"
# tuple      -> (1, 2, 3)
# range      -> range(10)
# bytes      -> b"abc"
# frozenset  -> frozenset({1,2,3})

# Difference:
# Mutable:
#   nums = [1,2,3]
#   nums[0] = 10          # Same object is modified.
#
# Immutable:
#   s = "hello"
#   s = "Hello"           # New string object is created.
#   s[0] = "H"            # TypeError

# -------------------- SLICING --------------------
# Syntax:
# sequence[start : stop : step]

# Examples:
# arr[:3]      -> first 3 elements
# arr[3:]      -> elements from index 3 onwards
# arr[:]       -> copy entire sequence
# arr[-2:]     -> last 2 elements
# arr[:-1]     -> everything except last element
# arr[::2]     -> every 2nd element
# arr[::-1]    -> reverse
# arr[::-2]    -> reverse, every 2nd element

# Slicing works on:
# ✅ list
# ✅ str
# ✅ tuple
# ✅ range
# ✅ bytes
# ✅ bytearray

# Slicing DOES NOT work on:
# ❌ dict
# ❌ set

# Note:
# Slicing creates a NEW object.
# Example:
# left = nums[:mid]
# right = nums[mid:]

# ===================== TIME COMPLEXITIES =====================
# O(1)      -> Array indexing, HashMap lookup
# O(log n)  -> Binary Search
# O(n)      -> Single loop
# O(n log n)-> Merge Sort, Timsort, Heap Sort
# O(n²)     -> Two nested loops
# O(n³)     -> Three nested loops
# O(n⁴)     -> Four nested loops
# O(2ⁿ)     -> Generate all subsets (Backtracking)
# O(n!)     -> Generate all permutations

# ===================== MERGE SORT =====================
# Merge Sort:
# 1. Divide the array into two halves.
# 2. Recursively sort each half.
# 3. Merge the two sorted halves.

# During merge:
# while i < len(left) and j < len(right):
#     compare left[i] and right[j]
#     append the smaller one

# After the loop:
# ans.extend(left[i:])
# ans.extend(right[j:])

# Why?
# One list may still have remaining elements.
# Only ONE of these slices can be non-empty because the loop
# stops when either left or right is exhausted.

# Swapping the two extend() lines does NOT affect correctness
# because one of them always extends an empty list.

a = 42
b = 3.14
c = "hello"
d = True
e = [1, 2, 3] # list is mutable, so it can be changed after creation
f = (1, 2, 3) # tuple is immutable, so it cannot be changed after creation
g = {"a": 1, "b": 2} # dict is mutable, so it can be changed after creation
h = {1, 2, 3} # set is mutable, so it can be changed after creation

print(a, b, c, d, e, f, g, h, '\n')
print(e[0], f[1], g['a'], '\n')
# print(e[0], f[1], g['a'], h[2], '\n')

# Tuple is immutable, so it cannot be changed after creation
# Tuple is ordered, so indexing is supported


# Set only stores unique values
# Set is unordered, so indexing is not supported
# Set is mutable, so it can be changed after creation

# mutable: can be changed after creation
# immutable: cannot be changed after creation

# diff b/w list and tuple
# list is mutable, tuple is immutable
# diff b/w dict and set
# set is mutable, so it can be changed after creation
# dict is mutable, so it can be changed after creation
# mutable vs immutable

for i in e:
    print(i)
print('\n')
for i in f:
    print(i)
print('\n')
for key, value in g.items():
    print(key, value)
print('\n')
for i in h:
    print(i)