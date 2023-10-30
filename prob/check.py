from itertools import permutations, combinations, combinations_with_replacement
print(list(permutations(['a','b', 'c'], 3)))
# print(list(combinations(['a','b','c'], 2)))

print(list(combinations_with_replacement(['a','b', 'c'], 3)))
print(list(combinations(['a','b', 'c'], 2)))
