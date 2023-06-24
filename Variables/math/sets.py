numbers = set()
for i in range(1, 6):
    numbers.add(i)
print(numbers)

numbers.discard(1)
numbers.discard(2)
numbers.discard(3)
print(numbers)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9, 0}

set1.update(set2)
print(set1)
