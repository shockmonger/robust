def fib(n):
	try:
		if n == 0:
			return 0;
		elif n ==1:
			return 1;
		elif n <0:
			return NotImplemented
		else:
			return fib(n-1)+fib(n-2)
	except TypeError as detail:
		raise TypeError(detail.__str__()+ ' got passed variable type wrong buddy')