import os
from collections import OrderedDict

ASCII_VALUES = {
	"S": '`',
	"E": '{'
}

class Node(object):
	def __init__(self, pos, char, parent = None):
		self.f = 0
		self.g = 0
		self.h = 0
		self.pos = pos
		# If elevations go from a-z, then S will lie on [z+1], which is {
		self.value = ord(ASCII_VALUES.get(char, char))
		self.parent = parent

	def IteratePath(self):
		if self.parent:
			yield from self.parent.IteratePath()

		yield self

def GetAdjacent(grid, position):
	x, y = position

	if x > 0:
		yield (x - 1, y)

	if y > 0:
		yield (x, y - 1)

	if x < len(grid[y]) - 1:
		yield (x + 1, y)

	if y < len(grid) - 1:
		yield (x, y + 1)

def FindPath(grid, start, end):
	open = OrderedDict()
	closed = {}

	open[start] = Node(start, grid[start[1]][start[0]])

	while any(open):
		current = open.popitem(last = False)[-1]
		closed[current.pos] = current

		if current.pos == end:
			return list(current.IteratePath())

		validAdjacent = [(x, y) for x,y in GetAdjacent(grid, current.pos) if ord(ASCII_VALUES.get(grid[y][x], grid[y][x])) - current.value <= 1]

		for adjacent in validAdjacent:
			if adjacent in closed:
				continue

			child = Node(adjacent, grid[adjacent[1]][adjacent[0]], current)
			child.g = current.g + 1
			child.h = sum(abs(a - b) for a,b in zip(adjacent, end))
			child.f = child.g + child.h        

			existingChild = open.get(adjacent, None)
			if existingChild != None and child.g > existingChild.g:
				continue

			open[child.pos] = child

	return []

def Solution(inputFile, scenic = False):
	with open(inputFile) as inFile:
		data = [l.strip() for l in inFile.readlines()]

	start = None
	extraStarts = []
	end = None
	for y, line in enumerate(data):
		if start == None:
			x = line.find("S")
			if x != -1:
				start = (x, y)

		if end == None:
			x = line.find("E")
			if x != -1:
				end = (x, y)

		if scenic:
			extraStarts.extend((x, y) for x, c in enumerate(line) if c == 'a')

		if start != None and end != None and not scenic:
			break

	starts = [ start ]
	if scenic:
		starts.extend(extraStarts)

	results = [len(list(FindPath(data, start, end))) for start in starts]

	# We knock off one for the starting node.
	return min(l for l in results if l > 0) - 1

def test():
	assert Solution("Input/Day12_Example.txt") == 31
	print(f"Part 1: {Solution('Input/Day12.txt')}")

	assert Solution("Input/Day12_Example.txt", scenic = True) == 29
	print(f"Part 2: {Solution('Input/Day12.txt', scenic = True)}")
