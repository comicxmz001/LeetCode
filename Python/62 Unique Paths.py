class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n==0:
        	return 0
        T = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
        for i in xrange(m):
        	for j in xrange(n):
        		if i ==0 and j ==0:
        			T[i+1][j+1] = 1
        		else:
        			T[i+1][j+1] = T[i+1][j] + T[i][j+1]
        return T[-1][-1]

if __name__ == '__main__':
	print Solution().uniquePaths(3,7)