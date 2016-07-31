#!/usr/bin/python

import collections

class KMP(object):
	"""
		Find and return the index of first occurance of substring
	"""
	def __init__(self, pat):
		"""
			pre-process pattern string
		"""
		self._pat = pat
		self._M = len(pat) # the number of states of DFA
		self._miss = [0 for i in range(self._M)] # set default_factory for __missing__ of defaultdict
		
		# build DFA (deterministic finite state automaton)
		self._dfa = collections.defaultdict(lambda: [0 for i in range(self._M)])
		self._dfa[self._pat[0]][0] = 1
		
		X = 0 
		
		for j, letter in enumerate(self._pat[1:],1): # pricess from state 1, to state self._M
			for c in self._dfa.keys():
				self._dfa[c][j] = self._dfa[c][X] # set mismatch case
			self._dfa[letter][j] = j + 1 # set match case
			X = self._dfa[letter][X] # update restart state
			
	def search(self, txt):
		"""
			Returns the idx of the 1st occurrrence of the pattern string in the text string.
		"""
		N = len(txt)
		i = 0 # index of txt string
		M = self._M
		j = 0 # index of dfa
		
		while i < N and j < M:
			j = self._dfa.get(txt[i],self._miss)[j]
			i += 1
			
		if j == M: return i - M  # if found
		return N
					

def main():
	k = KMP("123")
	
	assert k.search("alfjaksdjf;123adjfa;lsdfj") == 11
	assert k.search("a123") == 1
	
if __name__ == "__main__":
	main()