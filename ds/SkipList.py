class SkipList(object):
	"""
	An example implementation for SkipList
	"""

	class Node(object):
		"""Class of node in a skip list"""
		def __init__(self, value, level):
			self.Value = value
			self.Next = [None] * level
			self.Level = level

	def __init__(self, MaxLevel):
		self.levels = 1
		self.maxLevel = MaxLevel # set maximum level to 33
		self.head = self.Node(0, self.maxLevel)
		self.n = 0 

	
	def insert(self, value):
		# create a node
		node = self.Node(value, self._randLevel())

		# find a proper position
		cur = self.head
		
		for i in xrange(node.Level - 1, -1, -1): # from top to bottom
			while cur.Next[i] and cmp(value, cur.Next[i].Value) >= 0:
				cur = cur.Next[i]
			# reach the position that node.Value < cur.Next[i].Value, insert here
			node.Next[i] = cur.Next[i]
			cur.Next[i] = node

		self.n += 1
		return True


	def _randLevel(self):
		from random import uniform

		level = 1
		while uniform(0,1) < 0.5 and level < self.maxLevel:
			level += 1
			if level == self.levels + 1: 
				self.levels += 1
				break
		return level


	def contains(self, value):
		cur = self.head

		for i in xrange(self.levels -1, -1, -1):
			while cur.Next[i] and cmp(value, cur.Next[i].Value) >= 0:
				if cur.Next[i].Value == value: return True
				cur = cur.Next[i]
		return False
				

	def delete(self, value):
		cur = self.head
		found = False

		for i in xrange(self.levels - 1, -1, -1):
			while cur.Next[i] and cmp(value, cur.Next[i].Value) >= 0:
				if cur.Next[i].Value == value: 
					found = True
					cur.Next[i] = cur.Next[i].Next[i]
					break
				cur = cur.Next[i]
		
		return found

	def __str__(self):
		mystr = ""
		for level in xrange(self.levels):
			cur = self.head.Next[level]
			values = []
			while cur:
				values.append(str(cur.Value))
				cur = cur.Next[level]
			mystr += "Level {}: {}\n".format(str(level),"->".join(values))
		
		return mystr
	
	
	def __len__(self):
		return self.n

		

if __name__ == '__main__':
	import random
	l = SkipList(16)
	ran = lambda : random.randint(-100,200)
	seq = lambda x: x 
	for i in [seq(x) for x in xrange(1000)]:
		l.insert(i)
	print l.levels
	# l.delete(3)
	# print l