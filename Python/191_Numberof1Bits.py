class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
		# ex:       00000000000000000000000000001011 (11)
		# 						&
        #           00000000000000000000000000000001  (1)
        # will be   00000000000000000000000000000001
        # so numOnes will increment by 1.
        count = 0
        while n!=0:
	        count += n&1
	        n >>= 1 # shift n's bits to the right by 1.
        return count
        
foo = Solution()
print foo.hammingWeight(11)
#Answer should be 3