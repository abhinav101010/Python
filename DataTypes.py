# int
# float
# str
# bool
# list
# tuple
# dict
# set

a = 42
b = 3.14
c = "hello"
d = True
e = [1, 2, 3]
f = (1, 2, 3)
g = {"a": 1, "b": 2}
h = {1, 2, 3}

print(a, b, c, d, e, f, g, h, '\n')
print(e[0], f[1], g['a'], '\n')
# print(e[0], f[1], g['a'], h[2], '\n')

# mutable: can be changed after creation
# immutable: cannot be changed after creation

# diff b/w list and tuple
# list is mutable, tuple is immutable
# diff b/w dict and set
# dict is mutable, set is immutable
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