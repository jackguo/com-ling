#!/usr/bin/env python
from nltk import parse_cfg, ChartParser
from nltk.grammar import is_nonterminal, Nonterminal
from random import choice

def expand(symbol, grammar):
	if not is_nonterminal(symbol):
		return (symbol,)
	else:
		rule = choice(grammar.productions(lhs=symbol));
		return rule.rhs()

def expand_seq(SymbolTuple, grammar):
	return reduce(lambda x,y:x+y, [expand(s, grammar) for s in SymbolTuple])

def GenerateFrom(grammar):
	tupleSymbols = (grammar.start(),)
	while any([is_nonterminal(symbol) for symbol in tupleSymbols]):
		tupleSymbols = expand_seq(tupleSymbols, grammar)
	return tupleSymbols


grammar_file = open("snarxiv-python.txt", "r")
grammar_string = grammar_file.read()
grammar_file.close()

grammar = parse_cfg(grammar_string)

test1 = GenerateFrom(grammar)

print " ".join(test1)

parser = ChartParser(grammar)
parses = parser.nbest_parse(test1)
parses[0].draw()
