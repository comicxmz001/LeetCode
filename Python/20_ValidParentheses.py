class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		#Stack is easy solution. Complier basics.
		Stack = []
		pTable = {')':'(',']':'[','}':'{'}
		for i in s:
			if i in pTable.values():
				Stack.append(i)
			elif i in pTable.keys():
				if Stack == [] or pTable[i] != Stack.pop():
					return False
			else:
				return False
		#if Stack is empty, then all brackets matched
		return Stack == []

mystr = "{}{{[[]]}}"
print Solution().isValid(mystr)