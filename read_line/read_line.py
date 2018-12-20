#!/usr/bin/env python3

import argparse

parser=argparse.ArgumentParser()
parser.add_argument("filename", help="Provide a file name")
parser.add_argument("--line", "-l", type=int, help="Line number to read")

args=parser.parse_args()

try:
	f = open(args.filename, 'r')
except FileNotFoundError as err:
	print(err)

with f:
	if args.line:	
		lines = f.readlines()
		try:
			print(lines[args.line - 1].strip())
		except IndexError as err_index:
			print(err_index)
	else:
		print(f.read())
