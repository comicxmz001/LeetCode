class min_heap(object):
	"""docstring for heap"""
	def __init__(self, nums = []):
		self.s = nums
		self.PQ_SIZE = 10
		self.q = [-1 for x in xrange(self.PQ_SIZE+1)]
		self.n = 0
		if len(nums)>0:
			for num in nums:
				self.pq_insert(num)

			

	def pq_parent(self,n):
		"""return the index of parent item"""
		if n == 1:
			return -1 #error
		else:
			return n//2

	def pq_yong_child(self, n):
		"""n is the index of parent item"""
		return 2*n

	def pq_insert(self, x):
		"""insert item x into priorty queue"""
		if self.n == self.PQ_SIZE:
			self.q.append(-1)
			self.PQ_SIZE += 1
		self.n += 1
		self.q[self.n] = x
		self.bubble_up(self.n)

	def pq_swap(self, a, b):
		"""swap two items in priority queue"""
		self.q[a],self.q[b] = self.q[b], self.q[a]

	def bubble_up(self, n):		
		"""n is the index of newly inserted item"""
		parent = self.pq_parent(n)
		if parent == -1: # this is root item
			return
		if self.q[parent] > self.q[n]:
			self.pq_swap(n,parent)
			self.bubble_up(parent)

	def bubble_down(self,n):
		"""n is the index of newly inserted item"""

		min_index = n 
		left_child = self.pq_yong_child(n)

		if left_child <= self.n and self.q[min_index] > self.q[left_child]:
			min_index = left_child
		if left_child <= self.n and self.q[min_index] > self.q[left_child+1]:
			min_index = left_child+1
		if min_index != n:
			self.pq_swap(min_index,n)
			self.bubble_down(min_index)

	def extract_min(self):
		min_val = -1 # give a default value

		# if heap is not empty
		if self.n <= 0:
			print "Warning: empty priority queue!\n"
		else:
			min_val = self.q[1]
			self.q[1] = self.q[self.n]
			self.n -= 1
			self.bubble_down(1)

		return min_val

	def sort(self, mode = 0):
		if mode == 0: # ASC
			for i in xrange(self.n):
				self.s[i] = self.extract_min()
		return self.s


if __name__ == '__main__':
	s = [1918,2001,1941,1804,1865,1945,1963,1492,1783,1776]
	h = min_heap(s)
	print h.q[1:h.n+1]
	print h.sort()
