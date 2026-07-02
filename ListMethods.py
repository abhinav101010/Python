# List Methods

# append(x): Adds a single element x to the end of the list. 
# extend(iterable): Adds all elements from an iterable (like another list) to the end. 
# insert(i, x): Inserts element x at the specified index i. 

# pop([i]): Removes and returns the element at index i; if no index is provided, it removes and returns the last item. 
# remove(x): Removes the first occurrence of value x.  Raises an error if x is not found.
# clear(): Removes all elements from the list, leaving it empty. 

# index(x): Returns the index of the first occurrence of value x.  Raises an error if not found.
# count(x): Returns the number of times value x appears in the list. 

# sort(): Sorts the list in ascending order in-place. Can use reverse=True for descending order. 
# reverse(): Reverses the order of the list in-place.

# copy(): Returns a shallow copy of the list. 

# Note that methods like sort(), reverse(), append(), and extend() modify the original list and return None. For sorting without modifying the original, use the built-in sorted() function. 

a = [1, 2, 3, 4, 5]

print(a)
print(a.pop())
print(a.pop(0))
print(a)
