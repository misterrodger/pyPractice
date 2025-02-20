names = ['steve', 'bob', 'james', 'charles']

new_list = []

for n in names:
  if n.startswith('c'):
    new_list.append(n)

# print(new_list)

new_list2 = [
  n
  for n in names
  if n.startswith('c')
]

# print(new_list2)

num_list = [
  (a, b)
  for a in range(1, 4)
  for b in range(1, 4)
]

# print(num_list)

num_list2 = [1, 2, 3, 4]

num_list3 = [
  num * 2
  if num % 2 == 0
  else num
  for num in num_list2
]

# print(num_list3)

dict1 = {
  'name': 'steve',
  'age': 42
}

dict2 = {
  value: key
  for key, value in dict1.items()
}

print(dict2)