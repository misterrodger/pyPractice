from functools import reduce

def square_digits(num):
  num_map = map(lambda each: str(int(each)**2), tuple(str(num)))

  return ''.join(num_map)

def square_digits2(num):
  num_list = [
    str(int(x)**2)
    for x in str(num)
  ]

  return ''.join(num_list)


# with reduce
def pipe(value, *funcs):
    return reduce(lambda acc, f: f(acc), funcs, value)

def square_digits3(num):
    return pipe(
        str(num),
        lambda s: map(lambda d: int(d)**2, s),  
        lambda m: ''.join(map(str, m)),
        int
    )

print(square_digits3(81181))  # Output: 641181
