import math
import os
import re

class Monkey(object):
	RAW_PARSE_REGEX = re.compile(r"Monkey (?P<id>\d+):\s+Starting items: (?P<starters>[\d, ]+)\s+Operation: (?P<operation>.+)\s+Test: divisible by (?P<test>\d+)\s+If true: (?P<true>.+)\s+If false: (?P<false>.+)")

	OPERATIONS = {
		"+": lambda a, b: a + b,
		"-": lambda a, b: a - b,
		"*": lambda a, b: a * b,
		"/": lambda a, b: a / b
	}

	def __init__(self, raw):
		# We parse the living hell out of everything here, using one regex, 
		# so that our later calculations (which are repeated much more) are
		# a damn sight simpler.
		match = self.RAW_PARSE_REGEX.match(raw)
		assert match != None

		match = match.groupdict()
		self.id = int(match["id"])
		self.items = [int(x) for x in match["starters"].split(", ")]

		operation = match["operation"]
		assert operation.startswith("new =")
		self.operation = operation.split(" ")[2:]
		for i, node in enumerate(self.operation):
			if node.isnumeric():
				self.operation[i] = int(node)

		self.testDivisor = int(match["test"])

		assert match["true"].startswith("throw to monkey")
		self.targetIfTrue = int(match["true"].rsplit(" ", 1)[-1])

		assert match["true"].startswith("throw to monkey")
		self.targetIfFalse = int(match["false"].rsplit(" ", 1)[-1])

		self.numItemsInspected = 0
	
	def Inspect(self, worryLevel):
		a = self.operation[0] == "old" and worryLevel or self.operation[0]
		b = self.operation[-1] == "old" and worryLevel or self.operation[-1]

		operation = self.OPERATIONS.get(self.operation[1], None)
		assert operation != None

		return operation(a, b)

	def ProcessTurn(self, tooWorried):
		while any(self.items):
			item = self.items.pop(0)

			if tooWorried:
				item = self.Inspect(item) % self.commonDivisor
			else:
				item = int(self.Inspect(item) / 3)

			nextMonkey = item % self.testDivisor == 0 and self.others[self.targetIfTrue] or self.others[self.targetIfFalse]
			nextMonkey.items.append(item)

			self.numItemsInspected += 1

def Solution(inputFile, numTurns, tooWorried = False):
	with open(inputFile) as inFile:
		data = inFile.read()

	monkeys = [Monkey(definition) for definition in data.split("\n\n")]

	commonDivisor = None
	if tooWorried:
		commonDivisor = math.prod(set(m.testDivisor for m in monkeys))

	# Make it so that each monkey is aware of the others.
	for monkey in monkeys:
		monkey.others = {m.id:m for m in monkeys if m.id != monkey.id}

		if commonDivisor:
			monkey.commonDivisor = commonDivisor

	for _ in range(numTurns):
		for monkey in monkeys:
			monkey.ProcessTurn(tooWorried)

	return math.prod(sorted([m.numItemsInspected for m in monkeys], reverse = True)[:2])

def test():
	assert Solution("Input/Day11_Example.txt", 20) == 10605
	print(f"Part 1: {Solution('Input/Day11.txt', 20)}")

	assert Solution("Input/Day11_Example.txt", 10000, tooWorried = True) == 2713310158
	print(f"Part 2: {Solution('Input/Day11.txt', 10000, tooWorried = True)}")
