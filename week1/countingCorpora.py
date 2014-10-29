#!/usr/bin/python3

import sys
import os.path
import re
from collections import defaultdict
from collections import Counter

def findNLengthNTimes(list):
	for i in reversed(range(len(longestWord))):
		for word in listOrderedByLength:
			if len(word[0]) >= i and word[1] >= i:
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

	d = defaultdict(int);
	for line in myFile:
		for word in line.split():
			d[word] += 1
	c = Counter(d)
	# print (list(d.items()))
	print ("Total number of words:", sum(c.values()))
	print ("Total number of distinct words:", len(c))
	print ("Average of times words were used:", int(sum(c.values())/len(c)))
	print ("42nd most used words and how many times:", c.most_common(42)[41])

	listOrderedByLength = sorted(c.items(), key=lambda w: len(w[0]), reverse=True)
	longestWord = listOrderedByLength[0][0]
	print ("Longest word:", longestWord)
	print ("Biggest N (length and times)", findNLengthNTimes(listOrderedByLength))


