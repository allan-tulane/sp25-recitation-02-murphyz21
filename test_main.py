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

	# These are my three additional test cases
	assert work_calc(12, 4, 2, lambda n: n) == 148
	assert work_calc(22, 2, 2, lambda n: n*n) == 874
	assert work_calc(12, 3, 4, lambda n: 1) == 13


# def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	# res = compare_work(work_fn1, work_fn2)

	# print(res)

	
# def test_compare_span():
	# TO DO
