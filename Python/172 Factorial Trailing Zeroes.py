class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        count = 0
        while n>0:
        	count += n//5
        	n = n//5

        return count

if __name__ == '__main__':
	print Solution().trailingZeroes(25)
	# 1808548329