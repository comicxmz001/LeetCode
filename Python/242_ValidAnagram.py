class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #if len is different, then return false
        ls = len(s)
        lt = len(t)
        if ls != lt:
        	return False
        #Hash table
        hash_s = {}
        hash_t = {}
        for i in xrange(ls):
        	if s[i] in hash_s:
	        	hash_s[s[i]] += 1
	        else:
	        	hash_s[s[i]] = 1
	        if t[i] in hash_t:
	        	hash_t[t[i]] += 1
	        else:
	        	hash_t[t[i]] = 1
    	#if two dictionaries are same, s and t are anagrams
    	if hash_t == hash_s:
    		return True
    	else:
    		return False

s = ""
t = ""
foo = Solution()
print foo.isAnagram(s,t)