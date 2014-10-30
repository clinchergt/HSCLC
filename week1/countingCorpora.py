#!/usr/bin/python3

import sys
import os.path
from collections import defaultdict
from collections import Counter

def findNLengthNTimes(list):
	for i in reversed(range(len(longestWord))):
		for word, times in listOrderedByLength:
			if len(word) >= i and times >= i:
				return i
	return 0

usage = "Usage: specify the text file to be read as the *only* argument"

if len(sys.argv) != 2:
	print (usage)
	exit()

filename = sys.argv[1]

if not os.path.isfile(filename):
	print ("File doesn't exist. ", usage)
	sys.exit()

with open(filename) as myFile:

	print("Filename:", filename)

	c = Counter()
	for line in myFile:
		for word in line.split():
			c[word] += 1

	# print (list(d.items()))
	print ("Total number of words:", sum(c.values()))
	print ("Total number of distinct words:", len(c))
	print ("Average of times words were used:", int(sum(c.values())/len(c)))
	print ("42nd most used words and how many times:", c.most_common(42)[-1])

	listOrderedByLength = sorted(c.items(), key=lambda w: len(w[0]), reverse=True)
	longestWord = listOrderedByLength[0][0]
	print ("Longest word:", longestWord)
	print ("Biggest N (length and times)", findNLengthNTimes(listOrderedByLength))


