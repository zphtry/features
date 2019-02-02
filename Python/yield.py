# внутри функции просто собираются все yield'ы и то, что они yield'ят превращается в генератор

def yield_test():

  a = 1
  yield a

  a += 1
  yield a

  a += 1
  yield a

  a += 1
  yield a

for x in yield_test():
  print(x)

# 1, 2, 3, 4