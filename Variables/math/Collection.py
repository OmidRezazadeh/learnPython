from collections import Counter
import itertools

set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
#  اشتراک
# print(set1 & set2)
# print(set1.intersection(set2))
# اجتماع
# print(set1 | set2)
# print(set1.union(set2))
# تفاوت
# print(set1.difference(set2))
# print(set2.difference(set1))

# print(set2.symmetric_difference(set1))
# print(set2 ^set1)
# ضرب دکارتی
# print(list(product(set1, set2)))

# mmeber ship
# print(0 in set2)


# dis joint
# print(set2.isdisjoint(set1))

# subset
#  ایا اولی زیر مجموعه دومی هست یا نه
# print(set1.issubset(set2))
# result = []
# for lng in range(0, len(set1) + 1):
#     selection = list(itertools.combinations(set1,lng))
#     result.extend(selection)
#
# for x in result:
#     print(x)

nums = [1, 2, 5, 8, 6]

cnt = Counter(nums)

total = 0
for x in cnt:
    if cnt[x] == 1:
        total += x  

print(total)
