from itertools import permutations
#
# pencil_p = permutations('pencil')
# count = 0

# for per in pencil_p:
#     if per[0] == 'p':
#         count += 1
# print(count)

# for per in pencil_p:
#     per_join = ''.join(per)
#     if 'pen' in per_join:
#         count += 1
#
# print(count)
# prize = 0
# for per in permutations([1, 2, 3, 4]):
#     for q_id, p_id in enumerate(per, start=1):
#         if q_id == p_id:
#             prize += 1
# print(prize)

string = "BBBGGGGGG"
total = 0
for per in permutations(string):
    is_valid = 1
    for i in range(len([per]) - 1):
        if per[i] == per[i + 1] == 'B':
            is_valid = 0
            break
    total += is_valid
print(total)
