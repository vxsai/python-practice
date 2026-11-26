#CLI+LIVE API + CSV I/O

import sys
import csv
import requests
import datacore

def main():
	if len(sys.argv) < 2:
		sys.exit("Üsage: python pipeline.py [sites_csv]... ")

	results = []
	
	
