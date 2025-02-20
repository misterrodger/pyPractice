from pathlib import Path
import json

with open(Path.cwd() / 'pyCheatsheet/test_data.json', 'r') as new_file:
  print(json.load(new_file))

with open(Path.cwd() / 'pyCheatsheet/test_data.json', 'w') as edited_file:
  data = {
    'name': 'steve',
    'age': 42
  }
  json.dump(data, edited_file)