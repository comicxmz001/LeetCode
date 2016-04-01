class RedBlackBST(object):
	RED = True
	BLACK = False

	def __init__(self):
		self._root = None;
	class _Node(object):
		def __init__(self, key, val, color, N):
			self.key = key
			self.val = val
			self.left = None
			self.right = None
			self.color = color
			self.N = N

	# helper methods
	def __isRed(self, x):
		"""True if node is RED else False if BLACK"""
		return x is not None and x.color == RedBlackBST.RED # black if None

	def __size(self,x):
		"""number of node in subtree rooted at x"""
		return x.N if x is not None else 0

	def size(self):
		"""return the number of key-value pairs in this tree"""
		return self.__size(self._root)

	# standard BST search
	def get(self, key):
		return self.__get(self._root, key)

	def __get(self, x, key):
		while x is not None:
			cmp_keys = compareTo_keys(key, x.key)
			if cmp_keys < 0: 
				x = x.left
			elif cmp_keys > 0:
				x = x.right
			else: # find key, return value
				return x.val

	@staticmethod
	def compareTo_keys(keyA,keyB):
		return (keyA>keyB) - (keyA<keyB)

	############################################
	#	Red-black tree insertion
	###############################
	
	def put(self, key, val):
		self._root = self.__put(self._root,key,val)
		self._root.color = RedBlackBST.BLACK
		

	def __put(self, h, key, val):
		"""insert key-value pair into subtree rooted at h"""
		if h is None:
			return self._Node(key,val,RedBlackBST.RED,1)

		cmp_keys = RedBlackBST.compareTo_keys(key,h.key)

		# find right position to insert
		if cmp_keys < 0:
			h.left = self.__put(h.left, key, val)
		elif cmp_keys > 0:
			h.right = self.__put(h.right, key, val)
		else: # update value
			h.val = val

		# fix up any right leaning links (no REDs on right)
		# Three steps: rotateLeft? -> rotateRight? -> flipColors?
		# Then update N after each insertion
		
		if self.__isRed(h.right) and not self.__isRed(h.left):
			h = self.__rotateLeft(h)
		if self.__isRed(h.left) and self.__isRed(h.left.left):
			h = self.__rotateRight(h)
		if self.__isRed(h.left) and self.__isRed(h.right):
			self.__flipColors(h)
		h.N = self.__size(h.left) + self.__size(h.right) + 1

		return h
	###############################
	#	helper method for put
	################################
	def __rotateLeft(self,h):
		x = h.right
		h.right = x.left
		x.left = h
		x.color = h.color
		h.color = RedBlackBST.RED
		h.N = self.__size(h.left) + self.__size(h.right) + 1
		return x
	def __rotateRight(self,h):
		x = h.left
		h.left = x.right
		x.right = h
		x.color = h.color
		h.color = RedBlackBST.RED
		h.N = self.__size(h.left) + self.__size(h.right) + 1
		return x
	def __flipColors(self,h):
		h.color = RedBlackBST.RED
		h.left.color = RedBlackBST.BLACK
		h.right.color = RedBlackBST.BLACK


	######################################################
	#	traversal 
	####################################
	
	def display_bfs(self):
		import collections
		res = []
		q = collections.deque()
		q.append(self._root)
		while q:
			cur = q.popleft()
			if cur.left:
				q.append(cur.left)
			if cur.right:
				q.append(cur.right)
			res.append(cur.key)
		print res



if __name__ == '__main__':
	t = RedBlackBST()

	t.put('S','SSS')
	t.put('E','EEE')
	t.put('A','AAA')
	t.put('R','RRR')
	t.put('C','CCC')
	t.put('H','HHH')
	t.put('X','XXX')
	t.put('M','MMM')
	t.put('P','PPP')
	t.put('L','LLL')
	t.display_bfs()