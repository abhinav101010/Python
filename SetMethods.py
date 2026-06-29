# Set Methods

# add(element): Adds a single element; ignores duplicates.
# update(iterable): Adds multiple elements from lists, tuples, or other sets.
# remove(element): Deletes a specific element; raises KeyError if missing.
# discard(element): Deletes a specific element; does nothing if missing.
# pop(): Removes and returns an arbitrary element; raises KeyError if empty.
# clear(): Removes all elements, leaving the set empty. 
# issubset(other) or <=: Returns True if the set is a subset of another.
# issuperset(other) or >=: Returns True if the set is a superset of another.
# isdisjoint(other): Returns True if the sets have no elements in common.
# copy(): Returns a shallow copy of the set. 

a = set()
a.add(1)
a.add(2)
a.add(3)

print(a)

a.update([4, 5, 6])
print(a)

a.remove(3)
print(a)

a.discard(3)
print(a)

a.pop()
print(a)

a.clear()
print(a)

b = a.copy()
print(b)

print(a == b)
print(a is b)
print(a.issubset({1,2,3}))