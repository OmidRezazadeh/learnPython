count = 0
for num in range(100, 10000):
    if len(set(str(num))) != len(str(num)):
        count += 1

print(count)

