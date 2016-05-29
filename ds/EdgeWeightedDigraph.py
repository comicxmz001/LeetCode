class EdgeWeightedDigraph(object):
	"""An example implementation of EdgeWeightedDigraph"""

	class DirectedEdges(object):
		"""docstring for DirectedEdges"""
		def __init__(self, v, w, weight):
			self.__v = v
			self.__w = w
			self.__weight = weight

		def fromV(self):
			return self.__v

		def toV(self):
			return self.__w

		def weight(self):
			return self.__weight
			
	def __init__(self, V):
		self.__adj = [[]for _ in xrange(V)]
		self.__V = V
	
	def addEdge(self, v, w, weight):
		e = self.DirectedEdges(v, w, weight)
		self.__adj[e.fromV()].append(e)

	def adj(self, v):
		return self.__adj[v]

	def V(self):
		return self.__V


class SP(object):
	"""
	shortest path from s in edge weighted directed graph
	"""
	
	def __init__(self, G, s):
		self.__g = G
		self.__s = s
		self.__edgeTo = [None for _ in xrange(G.V())] 
		self.__distTo = [99990]*G.V()

	def distTo(self, v):
		"""length of the shortest path (from s) to v"""
		return self.__distTo[v]

	def pathTo(self, v):
		"""the shortest path (from s) to v"""
		from collections import deque
		path = deque()
		e = self.__edgeTo[v]
		while e:
			path.append(e)
			e = self.__edgeTo[e.fromV()]
		return path

	def relx(self, e):
		# relax an edge if a smaller path weight is found
		# type e : DirectedEdges()
		v = e.fromV()
		w = e.toV()
		if self.__distTo[w] > self.__distTo[v] + e.weight():
			self.__distTo[w] = self.__distTo[v] + e.weight()
			self.__edgeTo[w] = e

		
		
if __name__ == '__main__':
	def createDAG(file):
		f = open(file,"r")
		numV = f.readline()
		numE = f.readline() #not useful in python
		edges = f.readlines()
		f.close()
		g = EdgeWeightedDigraph(int(numV))
		for edge in edges:
			edge = edge.split()
			g.addEdge(int(edge[0]), int(edge[1]), float(edge[2]))
		return g

	G = createDAG("graphdata/tinyEWD.txt")
	s = 0
	sp = SP(G,s)

	for v in xrange(G.V()):
		line = "{} to {} ({}): ".format(s,v,sp.distTo(v))
		print line

	






