def disemvowel(str):
  return ''.join([
    x
    for x in str
    if x not in 'aeiouAEIOU'
    ])

print(disemvowel("This website is for losers LOL!" ))

# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
