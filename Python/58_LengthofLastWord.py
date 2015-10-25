class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.split()) == 0:
        	return 0
        return len(s.split()[-1])

if __name__ == '__main__':
	s = "       sdf"
	print Solution().lengthOfLastWord(s)