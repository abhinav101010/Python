a = 10
b = 20
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

a = 20
b = 10
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is not greater than b")

# Conditional expressions
result = "a is greater than b" if a > b else "a is not greater than b"
print(result)
