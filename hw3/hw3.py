#!/bin/python
from nltk.corpus import inaugural
from matplotlib import pyplot

files = inaugural.fileids()
numFile = len(files)

TTR = []
timeline = []
x = range(numFile)

for i in range(numFile):
	wds = inaugural.words(files[i])
	tps = set(wds)
	TTR += [float(len(tps))/len(wds)]
	if(i%3 == 0):
		timeline += [files[i].split('-')[0]]

pyplot.plot(x, TTR)
pyplot.xlabel('Year')
pyplot.ylabel('TTR')
pyplot.xticks(range(0, numFile, 3), timeline)
pyplot.show()
