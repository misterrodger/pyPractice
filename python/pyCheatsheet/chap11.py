import functools

def decorator_args_wrapper(prefix):
  def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      print(prefix, 'before func')
      print(func.__name__)
      func(*args, **kwargs)
      print('after func')
    return wrapper
  return my_decorator

@decorator_args_wrapper('testing')
def my_func(name):
  print('main func call', name)

my_func('steve')
