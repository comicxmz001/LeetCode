class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = "{0:032b}".format(n)
        reversedb = binary[::-1]
        return int(reversedb,2)

if __name__ == '__main__':
	print Solution().reverseBits(43261596)