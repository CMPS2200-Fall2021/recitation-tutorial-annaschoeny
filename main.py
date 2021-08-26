def sum_of_squares(a):
	sum = 0
	for x in a:
		sum += x*x
	return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
	assert sum_of_squares([2,4,6]) == 56

test_one()
test_two()
