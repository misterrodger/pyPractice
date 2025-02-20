import itertools
import operator

nums = [1, 2, 3, 4]

result = itertools.combinations(nums, 3)  # [1, 3, 6, 10]

print(list(result))
