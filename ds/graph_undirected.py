class graph(object):
	"""undirected graph class -- an implementation of Algorithm II"""
	def __init__(self, V):
		"""int V: number of vertices"""
		self._v = V
		self._e = 0
		self._adj = [[] for x in xrange(V)] # adjacency list
	
	def V(self):
		"""return the number of vertices"""
		return self._v

	def E(self):
		"""return the number of edges"""
		return self._e

	def adj(self, v):
		return self._adj[v]

	def degree(self,v):
		"""return the degree of vertex v"""
		return len(self._adj[v])

	def maxDegree(self):
		"""return the maximum degree of the graph"""
		maxD = 0
		for v in xrange(self.V()):
			maxD = len(self._adj[v]) if len(self._adj[v]) > maxD else maxD
		return maxD

	def averageDegree(self):
		"""return the average degree of the graph"""
		return 2*self.E()/self.V()

	def numberOfSelfLoops(self):
		"""return the number of loops in the graph"""
		count = 0
		for v in xrange(self.V()):
			for w in self._adj[v]:
				if w == v:
					count += 1
		return count

	def addEdge(self, v, w):
		"""add a new edge to graph
			v,w < self._v
		"""
		if v == w:
			self._adj[v].append(w)
		else:
			self._adj[v].append(w)
			self._adj[w].append(v)
		self._e += 1

	def dfs(self,v):
		"""
			depth-first-search traverse of graph
			int v: starting vertex
		"""
		visited = [False]*self.V()
		path = []
		self.__dfs(v, visited, path)
		return path

	def __dfs(self, v, visited, path):
		"""int v: current visiting vertex"""
		visited[v] = True
		path.append(v)
		for w in self.adj(v):
			if not visited[w]:
				self.__dfs(w,visited,path)

	def bfs(self, v):
		"""
			bread-first-search method for graph traversal
			int v: starting vertex
		"""
		from collections import deque
		visited = [False]*self.V()
		path = []
		q = deque()
		q.append(v)
		visited[v] = True
		while q:
			v = q.popleft()
			path.append(v)
			for w in G.adj(v):
				if not visited[w]:
					q.append(w)
					visited[w] = True
		return path

	def CC(self):
		"""connected components with bfs"""
		from collections import deque
		visited = [False]*self.V()
		ccGroup = [None]*self.V()
		group = -1
		q = deque()

		for v in xrange(self.V()):
			if not visited[v]:
				q.append(v)
				group += 1
				visited[v] = True
				ccGroup[v] = group
				while q:
					w = q.popleft()
					for i in G.adj(w):
						if not visited[i]:
							q.append(i)
							visited[i] = True
							ccGroup[i] = group
		return ccGroup



	

if __name__ == '__main__':

	def initExampleG1():
		G = graph(13)
		G.addEdge(0,1)
		G.addEdge(0,2)
		G.addEdge(0,5)
		G.addEdge(0,6)
		G.addEdge(3,4)
		G.addEdge(3,5)
		G.addEdge(4,5)
		G.addEdge(4,6)
		G.addEdge(7,8)
		G.addEdge(9,10)
		G.addEdge(9,11)
		G.addEdge(9,12)
		G.addEdge(11,12)
		return G
	def initExampleG2():
		G = graph(6)
		G.addEdge(0,1)
		G.addEdge(0,2)
		G.addEdge(0,5)
		G.addEdge(2,3)
		G.addEdge(2,4)
		G.addEdge(3,4)
		G.addEdge(3,5)
		return G

	G = initExampleG1()
	print G._adj
	# print G.dfs(0)
	# print G.bfs(0)
	print G.CC()