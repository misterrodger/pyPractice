import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

import traceback

class CustomException(Exception):
  pass

def divide(dividend, divisor):
  try:
    # raise Exception('error was raised')
    raise CustomException('raised custom exception')
    return dividend / divisor
  except (ZeroDivisionError, TypeError, CustomException) as error:
    print(error)
    print(traceback.format_exc())
    # print(traceback.format_stack())
    return 'sorry there was an error in the input'
  finally:
    print('end of code')

# print(divide('ok', 0))

def add(**kwargs):
  print(kwargs)
  # logging.debug('start of program')
  # try:
  #   assert int(num1), 'num1 has to be an int'
  #   return num1 + num2
  # except ValueError as error:
  #   print('error')

logging.disable()
print(add(num1='ok', num2=3))
