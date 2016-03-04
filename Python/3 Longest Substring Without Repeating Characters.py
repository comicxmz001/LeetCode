# Typical hash table problem

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        flag = [-1 for x in xrange(256)] # for 265 acii characters
        start = 0
        maxlen = 0
        for i in xrange(len(s)):
        	print flag[ord('a'):ord('d')+1], s[i] , i, start, maxlen

    		# check if this character has appeared in current substr
        	if flag[ord(s[i])] >= start: 
        		# if repeated, compare existing longest substr with current substr
        		maxlen = max(maxlen, i - start) 
        		# update starting positon of next substr 
        		start = flag[ord(s[i])] + 1
        	# update the lastest position of this character	
        	flag[ord(s[i])] = i

        maxlen = max(maxlen, len(s)-start)

        return maxlen

if __name__ == '__main__':
	s = "falsoiuelakhflkadhfih2983ryaliufhawp983yrp91#&(*#&hfieh(P(@*U(R*iu"
	print Solution().lengthOfLongestSubstring(s)
