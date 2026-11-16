#testing code to test day14-1 kinematics

from day14p1 import calc_ke

def test_standard():
	assert calc_ke(10, 2) == 20.0

	assert calc_ke(4,3) == 18.0


def test_negative():
	assert calc_ke(10,-2) == 20.0

def test_zero_n_negative_mass():
	assert calc_ke(0,50) == 0.0

	assert calc_ke(-5,50) == 0.0
