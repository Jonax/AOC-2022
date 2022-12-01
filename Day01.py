import os
import pytest

def IterateElves(calories):
	current = []

	for value in calories:
		if value == "":
			if any(current):
				yield current

			current = []
		else:
			current.append(int(value))

	if any(current):
		yield current

def Part1(inputFile):
	with open(inputFile) as inFile:
		data = [l.strip() for l in inFile.readlines()]

	return max(sum(e) for e in IterateElves(data))

def Part2(inputFile):
	with open(inputFile) as inFile:
		data = [l.strip() for l in inFile.readlines()]
	
	return sum(sorted([sum(e) for e in IterateElves(data)], reverse = True)[:3])

def test():
	assert Part1("Input/Day01_Example.txt") == 24000
	print(f"Part 1: {Part1('Input/Day01.txt')}")

	assert Part2("Input/Day01_Example.txt") == 45000
	print(f"Part 2: {Part2('Input/Day01.txt')}")
