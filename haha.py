

def tentotwo():
	a = int(input('Decimal number:'))
	c = ''
	while a:
		b = a % 2
		c += str(b)
		a = a // 2
	c = c[::-1]
	print('Binary number:%s' % c)

tentotwo()
