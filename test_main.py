from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

	## These are my three additional test cases
	assert simple_work_calc(8, 6, 4) == 20
	assert simple_work_calc(14, 6, 2) == 380
	assert simple_work_calc(20, 4, 4) == 56

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300

	# These are my three additional test cases for #3
	assert work_calc(12, 4, 2, lambda n: n) == 148
	assert work_calc(22, 2, 2, lambda n: n*n) == 874
	assert work_calc(12, 3, 4, lambda n: 1) == 13



def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	
	# Tests for Question 4
	# work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: 1)
	# work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: math.log(x))
	# work_fn3 = lambda n: work_calc(n, 2, 2, lambda x: x)

	# Tests for Question 5
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x**0.5)
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x**1.0)
	work_fn3 = lambda n: work_calc(n, 2, 2, lambda x: x**2.0)


	sizes = [10, 20, 50, 100, 1000, 5000, 10000]
	res = compare_work(work_fn1, work_fn2, work_fn3, sizes)


	print_results(res)


def test_compare_span():
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: 1)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: math.log(x))
	span_fn3 = lambda n: span_calc(n, 2, 2, lambda x: x)

	sizes = [10, 20, 50, 100, 1000, 5000, 10000]

	res = compare_span(span_fn1, span_fn2, span_fn3, sizes)
	
	print_results(res)