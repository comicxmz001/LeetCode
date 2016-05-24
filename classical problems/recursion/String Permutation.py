def strPermutation(word):
	res = []
	if len(word) == 1:
		res.append(word)
	else:
		for i in xrange(len(word)):
			permuteList = strPermutation(word[:i]+word[i+1:])
			for char in permuteList:
				res.append(word[i]+char)
	return res

print strPermutation('ABC')