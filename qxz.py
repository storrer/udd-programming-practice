# Which of the letters Q X and Z is least common?
from sys import maxsize

results = { 'Q': 0, 'X': 0, 'Z': 0}
with open('sowpods.txt', 'r') as file:
    for word in file:
        results['Q'] += word.count('Q')
        results['X'] += word.count('X')
        results['Z'] += word.count('Z')
"""
# test = ["QUEST", "ZEBRA", "QUICK", "XYLOPHONE"]
test = ['APPLE', 'AARDVARK', 'SIMPLE']
test_result = {'Q': 0, 'X': 0, 'Z': 0}
for word in test:
        test_result['Q'] += word.count('Q')
        test_result['X'] += word.count('X')
        test_result['Z'] += word.count('Z')
# print(results)

# print(test_result)
"""
least_common = []
minimum = maxsize
for k, value in results.items():
    if value < minimum:
         minimum = value
         least_common = [k]
    elif value == minimum:
         least_common.append(k)
    # print(k, value)

print(least_common)

test_result0 = {'Q': 0, 'X': 0, 'Z': 0} # ["Q","X","Z"]
test_result1 = {'Q': 999, 'X': 999, 'Z': 999} # ["Q","X","Z"]
test_result2 = {'Q': 5, 'X': 4, 'Z': 3} # ["Z"]
"""
least_common = []
minimum = maxsize
for k, value in test_result0.items():
    if value < minimum:
         minimum = value
         least_common = [k]
    elif value == minimum:
         least_common.append(k)
print(least_common)

least_common = []
minimum = maxsize
for k, value in test_result1.items():
    if value < minimum:
         minimum = value
         least_common = [k]
    elif value == minimum:
         least_common.append(k)
print(least_common)

least_common = []
minimum = maxsize
for k, value in test_result2.items():
    if value < minimum:
         minimum = value
         least_common = [k]
    elif value == minimum:
         least_common.append(k)
print(least_common)

"""
def get_least_common(counts: dict):
    least_common = []
    minimum = maxsize
    for k, value in counts.items():
        if value < minimum:
            minimum = value
            least_common = [k]
        elif value == minimum:
            least_common.append(k)
    return least_common

print(get_least_common(test_result0))
print(get_least_common(test_result1))
print(get_least_common(test_result2))