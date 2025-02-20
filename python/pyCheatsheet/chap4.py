my_list = ['steve', 'fred', 'lucy']
list_ages = 42, 23, 19

print(my_list[-2])

my_list[1] = 'george'

for index, item in enumerate(my_list):
  print(f'index {index} has item {item}')

for name, age in zip(my_list, list_ages):
  print (f'{name} is {age}')

result = 'george' not in my_list

print(result)

name1, name2, name3 = my_list

print(name1, name2, name3)

result1 = my_list.index('george')

print(result1)

print(sorted(list_ages, reverse=True))