import os

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

def Solution(inputFile, n = 1):
	with open(inputFile) as inFile:
		data = [l.strip() for l in inFile.readlines()]
	
	return sum(sorted([sum(e) for e in IterateElves(data)], reverse = True)[:n])

def test():
	assert Solution("Input/Day01_Example.txt") == 24000
	print(f"Part 1: {Solution('Input/Day01.txt')}")

	assert Solution("Input/Day01_Example.txt", 3) == 45000
	print(f"Part 2: {Solution('Input/Day01.txt', 3)}")
