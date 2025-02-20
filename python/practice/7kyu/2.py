filter_list = lambda l: list(filter(lambda x: type(x) is int, l))

print(filter_list([1, 2, 'a', 'b']))


list2 = ['1', '2']

print(
  list(map(int, list2))
      )
