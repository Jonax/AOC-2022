import os

def PartA(a, b):
	return max(a[0], b[0]) < min(a[1], b[1])

def PartB(a, b):
	return min(a[1], b[1]) >= max(a[0], b[0])

def Solution(func, inputFile):
	with open(inputFile) as inFile:
		data = [l.strip().split(',') for l in inFile.readlines()]

	return sum(func(*[[int(x) for x in range.split("-")] for range in line]) for line in data)

def test():
	assert Solution(PartA, "Input/Day04_Example.txt") == 2
	print(f"Part 1: {Solution(PartA, 'Input/Day04.txt')}")
	
	assert Solution(PartB, "Input/Day04_Example.txt") == 4
	print(f"Part 2: {Solution(PartB, 'Input/Day04.txt')}")
