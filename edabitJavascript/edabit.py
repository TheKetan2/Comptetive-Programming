def is_orthogonal(first, second):
	zipped = list(zip(first, second))
	add = 0
	for a in zipped:
		add += a[0]*a[1]
	return add == 0
	
		

	