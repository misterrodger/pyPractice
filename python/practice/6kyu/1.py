def solution(num):
  nums = range(num)

  list_comp = [
    x
    for x in nums 
    if x % 3 == 0
    or x % 5 == 0
    ]

  return sum(list_comp)

print(solution(10))

# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
