import os
from io import StringIO
from itertools import islice

LINE_WIDTH = 40
GRID_SIZE = LINE_WIDTH * 6

def ProcessSignals(commands):
	x = 1

	for command in commands:
		if command == "noop":
			yield x
		else:
			addx, _, value = command.partition(" ")

			if addx != "addx":
				raise Exception("Unrecognised command")

			for i in range(2):
				yield x

			x += int(value)

def DrawPixels(commands):
	line = StringIO()

	registers = iter(ProcessSignals(commands))
	for i in range(GRID_SIZE):
		if i % LINE_WIDTH == 0 and i > 0:
			yield line.getvalue()

			line = StringIO()

		register = next(registers)

		j = i % LINE_WIDTH
		line.write((j - 1 <= register <= j + 1) and "#" or ".")

	if line.tell() > 0:
		yield line.getvalue()

def Solution(inputFile, draw = False):
	with open(inputFile) as inFile:
		data = [l.strip() for l in inFile.readlines()]
	
	if not draw:
		positions = list(range(20, GRID_SIZE, LINE_WIDTH))
		strengths = list(islice(ProcessSignals(data), 19, GRID_SIZE - 1, LINE_WIDTH))

		return sum(m * n for m, n in zip(positions, strengths))

	return list(DrawPixels(data))

def test():
	assert Solution("Input/Day10_Example.txt") == 13140
	print(f"Part 1: {Solution('Input/Day10.txt')}")

	with open("Input/Day10_ExampleB.txt") as inFile:
		assert Solution("Input/Day10_Example.txt", draw = True) == [l.strip() for l in inFile.readlines()]
	print(f"Part 2: {Solution('Input/Day10.txt', draw = True)}")