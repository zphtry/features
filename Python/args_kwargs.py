# *args = я готов принять любое количество аргументов
def args_test(*args):
  for x in args:
    print(x)

args_test(2, 4, 5, 'hui', True, '')

# **kwargs = я готов принять любое количество аргументов с ключом
def kwargs_test(*kwargs):
  for x in args:
    print(x)

kwargs_test(a=2, pep8=4, told=5, AaA='hui', foo=True, bar='')