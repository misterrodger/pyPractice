def likes(names):
  match names:
    case []:
      return 'no one likes this'
    case [a]:
      return f'{a} likes this'
    case [a, b]:
      return f'{a} and {b} like this'
    case [a, b, c]:
      return f'{a}, {b} and {c} like this'
    case [a, b, *rest]:
      return f'{a}, {b} and {len(rest)} others like this'

print(likes(['Max', 'John', 'Mark', 'Steve']))

# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python