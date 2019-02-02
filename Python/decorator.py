# Декторатор -- это функция от функции.
# Он изменяет поведение основной функции, на основании того, что эта основная функция возвращает

def append_semicolon(func):
  return lambda: func() + ';'

@append_semicolon
def hello_decorated():
  return 'Hello, World!'

print(hello_decorated())
# Hello, World!;

# Также декоратор можно заменить эквивалентной конструкцией:
def hello_not_decorated():
  return 'Hello, World!'

print(append_semicolon(hello_not_decorated)())
# Hello, World!;