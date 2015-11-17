class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid)==0:
        	return 0
        if len(obstacleGrid[0]) == 0:
        	return 0

        T = [[0 for x in xrange(len(obstacleGrid[0])+1)] for x in xrange(len(obstacleGrid)+1)]

        for i in xrange(len(obstacleGrid)):
        	for j in xrange(len(obstacleGrid[0])):
        		if i == 0 and j == 0:
        			T[i+1][j+1] = 1 if obstacleGrid[i][j] == 0 else 0
        		elif obstacleGrid[i][j] == 1:
        			T[i+1][j+1] = 0
        		else:
	        		T[i+1][j+1] = T[i][j+1] + T[i+1][j]
        return T[-1][-1]

if __name__ == '__main__':
	grid = [
			[0,0,0],
			[0,1,0],
			[0,0,0]
			]
	grid1 = []
	grid2 = [[1]]
	print Solution().uniquePathsWithObstacles(grid2)