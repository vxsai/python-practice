#test code for day14p2 on reactor quest 

import pytest
from day14p2 import check_core

def test_stable():
	assert check_core(500) == "Stable."

def test_meltdown():
	with pytest.raises(ValueError):
		check_core(1200)
