#!/bin/python

import re

def tokenizeClitics(word):

	fullMatch = re.compile(r"(^(wali|lil|Al|li|wa))?(.+)((iy|ya|ka|ki|hi|hu|hA)$)")
	partialMatch = re.compile(r"(^(wali|lil|Al|li|wa))?(.+)((iy|ya|ka|ki|hi|hu|hA)$)?")

	res = fullMatch.search(word)
	if res == None:
		res = partialMatch.search(word)

	toprint = []
	for i in range(1, 6, 2):
		tmp = res.group(i)
		if tmp:
			toprint += [tmp]
	print " + ".join(toprint)


myFile = open("sampleArabic.txt", "r")
lines = [line[:-1] for line in myFile.readlines()]
myFile.close()

for line in lines:
	words = line.split()
	for word in words:
		tokenizeClitics(word)

