class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		stack = []
		path = path.split("/")
		for block in path:
			if block == "" or block == ".":
				continue
			elif block == "..":
				if stack:	stack.pop()
			else:
				stack.append(block)
		
		return "/" + "/".join(stack)
		

if __name__ == "__main__":
	p = "/.."
	print Solution().simplifyPath(p)