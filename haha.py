print('0000')
a = b = c = 0
for i in range(16):
  b += 1
  a += b ** 2
  c += b ** 3
  print(a, b, c)
