myBool = 6 > 5

myVar = not 6 > 5

print(myVar)

if not 6 > 5:
  print('lower')
else:
  print('ok')

testVar = 6

print('higher' if testVar > 5 else 'equal' if testVar == 5 else 'lower')

status_code = 202

match status_code:
  case 200 | 201:
    print('ok')
  case 400 | 404:
    print('not found')
  case _:
    print('none')

my_list = [1, 2, 3]

match my_list:
  case [a]:
    print(f"One item: {a}")
  case [a, *rest]:
    print(f"multiple cases: {a}, {rest}")

num = 42

match num:
  case str():
    print('a string')
  case int():
    if num > 40 and num < 50:
      print('an int')

data = 0

while data < 4:
  print(data)
  data += 1

for x in my_list:
  print(x)

for x in range(1, 9, 3):
  print(x)

for x in [1, 2, 3, 4, 5]:
  if x == 6:
    break
else:
  print('nothing equalled to 6')