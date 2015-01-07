#!/usr/bin/env python

import codecs
from nltk import UnigramTagger, BigramTagger, TrigramTagger
from math import ceil
from numpy import mean

corpusFile = codecs.open('estonianSample.txt', mode='r', encoding='latin-1')
sents = [[tuple(w.split('/')) for w in line[:-1].split()] for line in corpusFile.readlines()]
corpusFile.close()

n = len(sents)
step = int(ceil(n/10.0))

chunks = [sents[i:i+step] for i in range(0, n, step)]

res = []

for i in range(0, 10):
	training = reduce(lambda x,y:x+y,[chunks[j] for j in range(0, 10) if j != i])
	testing = chunks[i]

	t1 = UnigramTagger(training)
	t2 = BigramTagger(training, backoff = t1)
	t3 = TrigramTagger(training, backoff = t2)
	res += [t3.evaluate(testing)]

print "Average accuracy is: " + str(mean(res))
