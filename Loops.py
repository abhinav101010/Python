for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i * i)

i = 0

while i < 10:
    i += 1
    print(i)
    if i == 3:
        continue
    if i == 5:
        break

# python does not have do-while loops