import os
import re

def Solution(length, data = None, inputFile = None):
	if data == None:
		with open(inputFile) as inFile:
			data = inFile.read()

	for i in range(0, len(data) - length + 1):
		if len(set(data[i:i + length])) == length:
			return i + length

	return -1

def test():
	assert Solution(4, "mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
	assert Solution(4, "bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
	assert Solution(4, "nppdvjthqldpwncqszvftbrmjlhg") == 6
	assert Solution(4, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
	assert Solution(4, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
	print(f"Part 1: {Solution(4, inputFile = 'Input/Day06.txt')}")
	
	assert Solution(14, "mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
	assert Solution(14, "bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
	assert Solution(14, "nppdvjthqldpwncqszvftbrmjlhg") == 23
	assert Solution(14, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
	assert Solution(14, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
	print(f"Part 2: {Solution(14, inputFile = 'Input/Day06.txt')}")
