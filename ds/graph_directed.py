class Digraph(object):
	"""a class of directed graph"""
	def __init__(self, v):
		self._v = v
		self._adj = {x:[] for x in xrange(self._v)}



	def adj(self, v):
		"""vertices pointing from v"""
		return self._adj[v]
	def toString(self):
		string = "{\n"
		for key in self._adj.keys():
			string += "\t{}:{}\n".format(key,self._adj[key])
		string += "}"
		return string

	def V(self):
		"""number of vertices"""
		return self._v

	def E(self):
		"""number of edges"""
		count = 0
		for v in self._adj.keys():
			count += len(self._adj[v])
		return count

	def reverse(self):
		"""return a reversed digraph"""
		gR = Digraph(self.V())
		gR._adj = {x:[] for x in xrange(self._v)}
		for v in self._adj.keys():
			for w in self.adj(v):
				gR._adj[w].append(v)
		return gR

	def addEdge(self, v, w):
		"""add edge from v to w"""
		# print "Adding edge {x}->{y}".format(x=v,y=w)
		if not v in self._adj.keys():
			self._adj[v] = []
		self._adj[v].append(w)

	def dfs(self, v):
		marked = [False]*self.V()
		edgeTo = [None]*self.V()
		self._dfs(v,marked,edgeTo)
	
	def _dfs(self,v,marked,edgeTo):
		marked[v] = True
		print v
		for w in self.adj(v):
			if not marked[w]:
				edgeTo[w] = v
				self._dfs(w,marked,edgeTo)

	def postOrderDFS(self):
		"""returns a list of vertices in post order"""
		marked = [False]*self.V()
		path = []
		for v in xrange(self.V()):
			if not marked[v]:
				self._postOrderDFS(v, marked, path)
		path.reverse()
		return path


	def _postOrderDFS(self, v, marked, path):
		marked[v] = True
		for w in self.adj(v):
			if not marked[w]:
				self._postOrderDFS(w, marked, path)
		path.append(v)

	def strongComponents(self):
		"""
			returns a list of strong components marked by group id.
			The idea is do the post-order DFS on reversed graph, get a list of vertices.
			then bfs/dfs the normal graph to find connected components,
			according to the result of post-order DFS on reversed graph.
		"""
		from collections import deque
		marked = [False]*self.V()
		CC = [None]*self.V()
		group = 0
		q = deque()

		gR = self.reverse()

		for v in gR.postOrderDFS():
			# use BFS to find connected components
			if not marked[v]:
				q.append(v)
				marked[v] = True
				CC[v] = group
				while q:
					w = q.popleft()
					for x in self.adj(w):
						if not marked[x]:
							q.append(x)
							marked[x] = True
							CC[x] = group
				group += 1
		return CC
			




	def bfs(self, v):
		from collections import deque
		q = deque()
		q.append(v)
		marked = [False]*self.V()
		edgeTo = [None]*self.V()
		distTo = [None]*self.V()
		marked[v] = True
		distTo[v] = 0

		path = []

		while q:
			w = q.popleft()
			path.append(w)
			# print w, edgeTo[w], distTo[w]
			for x in self.adj(w):
				if not marked[x]:
					q.append(x)
					marked[x] = True
					edgeTo[x] = w
					distTo[x] = distTo[edgeTo[x]] + 1
		return path


# testing code
	
def exampleDigraph1():
	dg = Digraph(13)
	edgeList = [(0,1),(0,5),(2,0),(2,3),(3,2),(3,5),
				(4,2),(4,3),(5,4),(6,0),(6,4),(6,8),
				(6,9),(7,6),(7,9),(8,6),(9,10),(9,11),
				(10,12),(11,4),(11,12),(12,9)]
	for pair in edgeList:
		dg.addEdge(pair[0],pair[1])	
	return dg

if __name__ == '__main__':
	dg = exampleDigraph1()
	# print dg.toString()
	# print dg.E()
	# dg.dfs(7)
	print dg.bfs(7)
	gR = dg.reverse()
	# print gR.toString()
	# print gR.postOrderDFS()
	# print dg.strongComponents()
	


	