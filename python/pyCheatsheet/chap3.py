
def myFunc(name, age):
  return name, age

print(myFunc(name='Steve', age=42))

num = 1

def myFunc2():
  global num
  num += 1
  print(num)

myFunc2()

add = lambda x, y: x + y

print(add(2, 3))


addPartial = lambda x: lambda y: x + y 

addTwo = addPartial(2)
result = addTwo(4)

print(result)