

my_list = [1, 3, 2, 4]
list_2 = ['name', 'age']

greaterThan2 = lambda x : x > 2

result = list(filter(greaterThan2, my_list))

print(result)

obj = {
  "name": "steve",
  "age": 25
}

print(list(enumerate(obj)))

# print(hash(obj))

# print(max('23534'))

# print(len('sdfgsg'))

# print(repr(obj))
# print(str(obj))

# print(sorted(my_list))

# print(sum(my_list))

# print(list(zip(my_list, list_2)))

# print(ascii(obj))

# print(complex(1005624678965234892))

dict1 = dict(name="Steve", age=42)
dict2 = dict([['name', 'steve'], ['age', 42]])
dict3 = dict([('name', 'steve'), ('age', 42)])

keys = ['name', 'age']
vals = ['steve', 42, 34, 42]
dict4 = dict(zip(keys, vals))

print(dict1)
print(dict2)
print(dict3)
print(dict4)

# print(dir(dict3))

# print(divmod(5, 2))

print(list(enumerate(dict1)))

print(hex(1234367765))

print(id(obj))

# print(locals())

print(object())

print(pow(4, 3))

print(property(obj))

print(list(reversed(vals)))

print(round(4.1345, 2))

print(set(vals))

print(vals[slice(1, 3)])

print(sum([1, 2, 3, 'A']))

# print(tupl)

