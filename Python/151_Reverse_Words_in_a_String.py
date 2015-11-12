class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Method 1, 44ms
        return " ".join(reversed(s.split()))

        # Method 2, 40ms with slicing operator, where -1 is step. 
        # return " ".join(s.split()[::-1]
if __name__ == '__main__':
	s = "the sky is blue"
	print Solution().reverseWords(s)