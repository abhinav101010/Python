# dictionaries Methods

# get(key, default): Returns the value for a key if it exists, or a specified default value (or None) if it does not, avoiding KeyError exceptions. 
# keys(): Returns a view object displaying a list of all dictionary keys. 
# values(): Returns a view object displaying a list of all dictionary values. 
# items(): Returns a view object containing a list of tuples for each key-value pair. 

# update([other]): Updates the dictionary by adding key-value pairs from another dictionary or iterable, overwriting existing keys. 
# setdefault(key, default): Returns the value for the key if it exists; if not, it inserts the key with the specified default value. 
# pop(key, default): Removes the specified key and returns its value; if the key is missing, returns the default value if provided. 
# popitem(): Removes and returns the last inserted key-value pair as a tuple (raises KeyError if empty). 
# clear(): Removes all items from the dictionary, leaving it empty. 

# copy(): Returns a shallow copy of the dictionary. 
# fromkeys(iterable, value): A class method that creates a new dictionary with keys from an iterable and values set to a specified default value. 

a = {"name": "Abhinav", "age": 18, "city": "Gurugram", "occupation": "Software Engineer"}

print(a)
print(a.items())
print(a.keys())
print(a.values())
print(a.pop("name")) # pops the specified key and returns its value as a result
print(a)
print(a.popitem()) # pops last item and returns the removed item as a tuple
print(a)
print(a.copy()) # returns a shallow copy of the dictionary
a.clear() # removes all items from the dictionary
print(a)
print(a.fromkeys(["name"], "Abhinav"))
a.update({"name": "Abhinav Yadav"})
print(a)
a.setdefault("name", "Abhinav Yadav")
print(a)