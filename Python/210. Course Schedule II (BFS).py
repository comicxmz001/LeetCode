import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        #bfs
        inAdj = {x:set() for x in xrange(numCourses)}
        adj = {x:set() for x in xrange(numCourses)}
        
        for x, y in prerequisites:
            inAdj[x].add(y)
            adj[y].add(x)
        dq = collections.deque()
        # get all 0 in degree nodes
        for i in xrange(numCourses):
            if not inAdj[i]:
                dq.append(i)
        
        count = 0
        res = []
        
        while dq:
            node = dq.popleft()
            res.append(node)
            count += 1
            for v in adj[node]:
                inAdj[v].remove(node)
                if not inAdj[v]:
                    dq.append(v)
        return res if count == numCourses else []

if __name__ == '__main__':
    print Solution().findOrder(2,[[0,1],[1,0]])