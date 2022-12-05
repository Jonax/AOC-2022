import os
import re

MOVEMENT_REGEX = re.compile(r"move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)")

def ParseStacks(data):
	lines = [l.rstrip() for l in data.split("\n")]

	# Build the stacks using the last row.
	line = lines[-1]
	stackX = {int(line[x]):x for x in range(1, len(line), 4)}

	# All crates in a stack have the exact same x-coordinate, and in a 
	# predictable manner. 
	# So, we extract each crate's value from that position, and throw out
	# the rest.
	# We also go in reverse line order so that bottom is handled first; 
	# we're treating these like stacks.
	stacks = {i:[] for i in stackX.keys()}
	for line in lines[-1::-1]:
		if line == "":
			break

		for i, x in stackX.items():
			if len(line) <= x:
				continue

			value = line[x]
			if value == " ":
				continue

			stacks[i].append(value)

	return stacks

def ParseMoves(data):
	for match in MOVEMENT_REGEX.finditer(data):
		yield {k:int(v) for k,v in match.groupdict().items()}

def Solution(inputFile, multiple = False):
	with open(inputFile) as inFile:
		data = inFile.read()

	# Stack & movement data are split by the only blank line in the input,
	# so split on that to get each set and parse separately.
	stackData, _, moveData = data.partition("\n\n")

	stacks = ParseStacks(stackData)
	for move in ParseMoves(moveData):
		moving = stacks[move["from"]][-move["count"]:]
		del stacks[move["from"]][-move["count"]:]

		# Same process for both parts, just different order direction
		if not multiple:
			moving.reverse()

		stacks[move["to"]].extend(moving)

	return "".join(s[-1] for s in stacks.values())

def test():
	assert Solution("Input/Day05_Example.txt") == "CMZ"
	print(f"Part 1: {Solution('Input/Day05.txt')}")
	
	assert Solution("Input/Day05_Example.txt", multiple = True) == "MCD"
	print(f"Part 2: {Solution('Input/Day05.txt', multiple = True)}")
