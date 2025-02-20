def get_count(str):
  result = 0

  for letter in str:
    if letter in 'aeiou':
      result += 1

  return result

print(get_count('abecdi'))

# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python