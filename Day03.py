import os

def PartA(rucksacks):
	for rucksack in rucksacks:
		n = len(rucksack)
		assert n % 2 == 0

		inBoth = set(rucksack[:n // 2]) & set(rucksack[n // 2:])

		assert len(inBoth) == 1
		yield next(iter(inBoth))

def PartB(rucksacks):
	assert len(rucksacks) % 3 == 0

	for i in range(0, len(rucksacks), 3):
		group = [set(r) for r in rucksacks[i:i + 3]]
		inAll = set.intersection(*group)

		assert len(inAll) == 1
		yield next(iter(inAll))

def Solution(func, inputFile):
	with open(inputFile) as inFile:
		data = [l.strip() for l in inFile.readlines()]

	return sum((n.isupper() and 26 or 0) + (ord(n.upper()) - ord("A")) + 1 for n in func(data))

def test():
	assert Solution(PartA, "Input/Day03_Example.txt") == 157
	print(f"Part 1: {Solution(PartA, 'Input/Day03.txt')}")

	assert Solution(PartB, "Input/Day03_Example.txt") == 70
	print(f"Part 2: {Solution(PartB, 'Input/Day03.txt')}")
