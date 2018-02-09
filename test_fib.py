from fib import *

def test_fib0():
	obs = fib(0)
	exp = 0
	assert obs == exp


#create a function to test fib(1)
def test_fib1():
	obs = fib(1)
	exp = 1
	assert obs == exp


#function to test standard behavior

def test_fib():
	obs = fib(6)
	assert obs ==8


def test_negative():
	obs=fib(-4)
	exp = NotImplemented
	assert obs == exp