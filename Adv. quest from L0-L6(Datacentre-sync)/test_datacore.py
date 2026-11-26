#Automated QA suite  

import pytest
from datacore import c_to_f, classify_cooling, extract_temp

def test_c_to_f():
	assert c_to_f(0) == 32.0
	assert c_to_f(25) == 77.0
	with pytest.raises(ValueError):
		c_to_f(-300)

def test_classify_cooling():
	assert classify_cooling(35.0) == "HIGH COOLING"
	assert classify_cooling(20.0) == "NOMINAL"
	assert classify_cooling(10.0) == "LOW COOLING"


def test_extract_temp():
	test_payload = {"current_weather": {"temperature": 22.5}}
	assert extract_temp(test_payload) == 22.5

	with pytest.raises(KeyError):
		extract_temp({})
