class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A-Z:65-90 || a-z:97-122 
        # ord('A') = 65, chr(65)=A
        n = len(s)
        if n == 0:
        	return 0
        result = 0
        for x in xrange(0, n):
        	asc2 = ord(s[n-1-x])
        	if 96<asc2<123:
        		asc2 -= 32
        	result += (26**x)*(asc2-64)
        return result


        
s = ""
foo = Solution()
print foo.titleToNumber(s)