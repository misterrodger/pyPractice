from pathlib import Path

# print(Path.cwd())

# result = (Path.cwd() / 'pyCheatsheet' / 'testing' / 'deep' / 'testing').mkdir(parents=True)

# print(result)

# with open(Path.cwd() / 'pyCheatsheet/data.txt') as test_file:
#   for line in test_file:
#     print(line)

with open(Path.cwd() / 'pyCheatsheet/new_file.txt', 'w') as new_file:
  new_file.write('test text here')