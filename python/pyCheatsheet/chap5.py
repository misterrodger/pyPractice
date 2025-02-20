import pprint

my_dict = {
  'name': 'steve',
  'age': 42,
  'job': 'CEO'
}

# print(my_dict)

my_dict['location'] = 'New York City'

# print(my_dict)

# print(my_dict['age'])

values = my_dict.values()

# print(values)

# for key, value in my_dict.items():
#   print(key, value)

result = my_dict.get('nrame', 'no name found')

# print(result)

my_dict.setdefault('nrame', 'no value for nrame')

# print(my_dict['nrame'])

# print(my_dict.popitem())
# print(my_dict.pop('age'))

# del my_dict['name']

# print(my_dict)

if 'name' in my_dict:
  print(my_dict)

# pprint.pprint(my_dict)

obj_2 = { 'level': 'admin' }

result2 = { **my_dict, **obj_2 }

print(result2)