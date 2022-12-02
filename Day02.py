import os

def SimulateMoveA(opponentMove, myMove):
	opponentId = "ABC".index(opponentMove)
	mineId = "XYZ".index(myMove)

	result = mineId - opponentId
	
	score = 0
	if result in [1, -2]:
		score += 6		# WIN
	elif result in [-1, 2]:
		pass			# DRAW
	else:
		score += 3		# LOSS

	return score + mineId + 1

def SimulateMoveB(opponentMove, requiredResult):
	opponentId = "ABC".index(opponentMove)
	resultId = "XYZ".index(requiredResult) - 1

	requiredMove = (opponentId + resultId) % 3
	
	return ((resultId + 1) * 3 + requiredMove + 1)

def Solution(func, inputFile):
	with open(inputFile) as inFile:
		data = [l.strip().partition(" ") for l in inFile.readlines()]
	
	return sum(func(r[0], r[-1]) for r in data)

def test():
	assert Solution(SimulateMoveA, "Input/Day02_Example.txt") == 15
	print(f"Part 1: {Solution(SimulateMoveA, 'Input/Day02.txt')}")

	assert Solution(SimulateMoveB, "Input/Day02_Example.txt") == 12
	print(f"Part 2: {Solution(SimulateMoveB, 'Input/Day02.txt')}")