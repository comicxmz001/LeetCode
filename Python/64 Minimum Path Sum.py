# Typical DP problem. It's nature is shortest path finding in graph theory.
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
        	return 0
        if len(grid[0]) == 0:
        	return 0
        T = [[2**16 for x in xrange(len(grid[0])+1)] for x in xrange(len(grid)+1)]
        
        for i in xrange(len(grid)):
        	for j in xrange(len(grid[0])):
        		if i==0 and j==0:
        			T[i+1][j+1] = grid[i][j]
        		else:
	        		T[i+1][j+1] = min(T[i+1][j],T[i][j+1]) + grid[i][j]
       	return T[-1][-1]

if __name__ == '__main__':
	grid = [
			[0,8,7,4,2],
			[4,6,5,3,1],
			[8,9,1,4,5],
			[3,8,0,8,7]
			]
	print Solution().minPathSum(grid)