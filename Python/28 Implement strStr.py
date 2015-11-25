class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
        	return 0
        if len(haystack) < len(needle):
        	return -1
        for i in xrange(len(haystack)):
        	if i + len(needle) > len(haystack):
        		return -1
        	if haystack[i] != needle[0] or haystack[i+len(needle)-1] != needle[-1]:
        		continue
        	else:
        		j=0
	        	while j < len(needle) and i+j < len(haystack):
	        		if haystack[i+j] != needle[j]:
	        			break
	        		j += 1
	        		if j == len(needle):
	        			return i
        return -1

if __name__ == '__main__':
	
	s1 = ""
	s2 = ""
	s3 = ""
	print Solution().strStr(s1,s2)

