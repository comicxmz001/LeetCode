class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
        	digit = (n-1)%26
        	res = chr(digit+ord('A')) + res
        	n = (n-1)//26
        	# print digit,n
        return res

if __name__ == '__main__':
	print Solution().convertToTitle(1001234)