import os
import json

class Directory(object):
	def __init__(self, name, parent = None):
		self.subDirs = []
		self.files = {}
		self.name = name
		self.parent = parent

		self.fullPath = parent != None and f"{parent.fullPath}/{self.name}" or self.name

	def Subdirectory(self, dirName):
		if dirName in self.subDirs:
			return self.subDirs[dirName]

		subDir = Directory(dirName, self)
		self.subDirs.append(subDir)

		return subDir

	def AllSubfiles(self):
		descendants = []

		for subDir in self.subDirs[-1::-1]:
			for subResult in subDir.AllSubfiles():
				yield subResult
				descendants.extend(subResult["files"])

		dirFiles = [
		{
			"name": k, 
			"size": v,
			"dirPath": self.fullPath
		} for k,v in self.files.items()]

		# set() doesn't accept a key function, so instead we convert to JSON and
		# build a dictionary with them with keys. The resulting values are guaranteed
		# to then be unique. 
		uniqueEntries = {json.dumps(f):f for f in descendants + dirFiles}

		yield {
			"path": self.fullPath,
			"files": list(uniqueEntries.values())
		}

def ParseCommands(commands):
	current = None
	for command in commands:
		command = command.split(" ")

		if command[0] == "$":
			if command[1] == "cd":
				if command[2] == "/":
					current = Directory("/")
					root = current
				elif command[2] == "..":
					current = current.parent
				else:
					current = current.Subdirectory(command[2])
		else:
			if command[0] != "dir":
				current.files[command[-1]] = int(command[-2])

	return root

def Solution(inputFile, delete = False):
	with open(inputFile) as inFile:
		data = [l.strip() for l in inFile.readlines()]

	root = ParseCommands(data)

	dirSizes = {d["path"]:sum(f["size"] for f in d["files"]) for d in root.AllSubfiles()}

	if not delete:
		return sum([size for name,size in dirSizes.items() if size <= 100000])

	# 70MB space total, 30MB needed, means that space used needs to be less than 40GB
	spaceToDelete = dirSizes["/"] - 40000000
	assert spaceToDelete > 0
	
	return min(v for v in dirSizes.values() if v >= spaceToDelete)

def test():
	assert Solution("Input/Day07_Example.txt") == 95437
	print(f"Part 1: {Solution('Input/Day07.txt')}")
	
	assert Solution("Input/Day07_Example.txt", delete = True) == 24933642
	print(f"Part 2: {Solution('Input/Day07.txt', delete = True)}")
