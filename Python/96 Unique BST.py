class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = {0:1,1:1}
        
        # Bottom top DP
        for i in xrange(2,n+1): #calculate T[n]
        	T[i] = 0
        	for j in xrange(1,i+1): #calculate T[j]
        		T[i] += T[j-1]*T[i-j]  #  T[i] = T[0]*T[n-1] + ...+ T[n-1]*T[0]
        return T[n]

        

# https://www.quora.com/Given-n-how-many-structurally-unique-BSTs-binary-search-trees-that-store-values-1-to-n-are-there
if __name__ == '__main__':
	print Solution().numTrees(6)