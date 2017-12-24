"""
A simple python script to generate a non-repeating permutation.
Suitable for Chirstmas present exchange.
"""
import random
import sys

def Shuffle(Member):
	ShuffledList = Member[:]
	while True:
		random.shuffle(ShuffledList)
		for original, shuffled in zip(Member, ShuffledList):
			if original == shuffled:
				break
		else:
			return ShuffledList
if 1 == len(sys.argv):
	print ("Usage : python3 Exchange.py ItemA ItemB ItemC ...")
	exit()

Member = sys.argv[1:]
Shuffled = Shuffle(Member)

for index in range(len(Member)):
	print(Member[index] + " --> " + Shuffled[index])
