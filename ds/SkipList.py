class SkipList(object):
	"""
	An example implementation for SkipList
	"""

	class Node(object):
		"""Class of node in a skip list"""
		def __init__(self, value, level):
			self.Value = value
			self.Next = [None] * level
			self.level = level

	def __init__(self):
		self._rand = 0
		self._levels = 1
		self.maxLevel = 33 # set maximum level to 33
		self._head = self.Node(0, self.maxLevel)
		self._n = 0 

	
	def insert(self, value):
		# create a node
		node = self.Node(value, self._randLevel())

		# find a proper position
		currHead = self._head
		updated = [None] * self.maxLevel

		for i in xrange(self._levels - 1, -1, -1): # from top to bottom
			while currHead.Next[i] and cmp(value, currHead.Next[i].Value) > 0:
				currHead = currHead.Next[i] # traverse on level i
			updated[i] = currHead
		
		currHead = currHead.Next[0] # ???
		if currHead and value == currHead.Value:
			return True
		
		# update list level if node becomes a new head
		if node.level > self._levels:
			for i in xrange(self._levels, node.level):
				updated[i] = self._head
			self._levels = node.level

		# insert into the SkipList (after updated[i])
		for i in xrange(node.level):
			node.Next[i] = updated[i].Next[i]
			updated[i].Next[i] = node
		
		self._n += 1

		# print l
		return True


	def _randLevel(self):
		from random import uniform

		level = 1
		while uniform(0,1) < 0.5 and level < self.maxLevel:
			level += 1
			if level == self._levels + 1: break
		return level


	def contains(self, value):
		cur = self._head

		for i in xrange(self._levels -1, -1, -1):
			while cur.Next[i] and cmp(value, cur.Next[i].Value) >= 0:
				if cur.Next[i].Value == value: return True
				cur = cur.Next[i]
		return False
				

	def delete(self, value):
		cur = self._head
		found = False

		for i in xrange(self._levels - 1, -1, -1):
			while cur.Next[i] and cmp(value, cur.Next[i].Value) >= 0:
				if cur.Next[i].Value == value: 
					found = True
					cur.Next[i] = cur.Next[i].Next[i]
					break
				cur = cur.Next[i]
		
		return found

	def __str__(self):
		mystr = ""
		for level in xrange(self._levels):
			cur = self._head.Next[level]
			values = []
			while cur:
				values.append(str(cur.Value))
				cur = cur.Next[level]
			mystr += "Level {}: {}\n".format(str(level),"->".join(values))
		
		return mystr
	
	
	def __len__(self):
		return self._n

		

if __name__ == '__main__':
	import random
	l = SkipList()
	ran = lambda : random.randint(-100,200)
	seq = lambda x: x 
	for i in [seq(x) for x in xrange(10)]:
		l.insert(i)
	print l
	l.delete(3)
	print l