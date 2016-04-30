class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		if numCourses < 2:
			return True
		marked = [0]*numCourses # 0 -> unprocessed, 1-> being processed, 2 -> processed
		adj = [[] for _ in xrange(numCourses)]

		for x,y in prerequisites:
			adj[x].append(y)

		for v in xrange(numCourses):
			if not self.dfs(v, marked, adj):
				return False

		return True
		
	def dfs(self, v, marked, adj):
		if marked[v] == 1: # cycle detected
			return False
		# it has been proven that vertex v and its successors are not contained in any cycle
		if marked[v] == 2:	 
			return True
		# start processing vertex v (marked[v] == 0)
		marked[v] = 1
		for w in adj[v]:
			if not self.dfs(w, marked, adj):
				return False
		marked[v] = 2
		return True



if __name__ == '__main__':
	numCourses = 3
	prerequisites = [[1,0],[2,0],[1,2]]
	print Solution().canFinish(numCourses,prerequisites)
