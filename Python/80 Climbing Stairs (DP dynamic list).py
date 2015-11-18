class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [1,1]
        for i in xrange(2,n+1):
        	T.append(T[i-1] + T[i-2]) # faster, with 36ms, predefined with 40ms.
        return T[n]

#  T[i] is the sum of T[i-1] (plus 1 step to reach end) 
#  and T[i-1] (plus 2 steps to reach end)


if __name__ == '__main__':
	print Solution().climbStairs(5)