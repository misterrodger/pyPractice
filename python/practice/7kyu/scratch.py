arr = [1, 2, 3, 4]

def pipeline(value):
  return lambda fn: {
    'result': value,
    'map': pipeline(fn(value))
  }

def process(input):
  return pipeline(input)['result']()

print(process(arr))
