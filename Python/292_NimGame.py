class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n >= 4:
        	return n%4 != 0
    	return True

n = 24
print Solution().canWinNim(n)