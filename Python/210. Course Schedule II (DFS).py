
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        #dfs
        inAdj = {x:set() for x in xrange(numCourses)}
        adj = {x:set() for x in xrange(numCourses)}
        
        for x, y in prerequisites:
            inAdj[x].add(y)
            adj[y].add(x)
        stack = []
        # get all 0 in degree nodes
        for i in xrange(numCourses):
            if not inAdj[i]:
                stack.append(i)
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node)
            for v in adj[node]:
                inAdj[v].remove(node)
                if not inAdj[v]:
                    stack.append(v)
            inAdj.pop(node)
        return res if len(res) == numCourses else []

if __name__ == '__main__':
    print Solution().findOrder(2,[[0,1],[1,0]])