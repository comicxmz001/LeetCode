class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
        	return res
        length = len(strs[0])
        # get the length of string
        for string in strs:
        	length = length if length < len(string) else len(string)

        # find longest common prefix
        for i in xrange(length):
        	k = strs[0][i]
        	for string in strs:
        		if string[i] != k:
        			k = ""
        			break
        	if k != "":
	        	res += k
	        else:
	        	break
        return res





if __name__ == '__main__':
	strs = ["a 1sdbbb","a 1sd12049urj","a 1iojadsflk","a 1b"]
	strs1 = []
	strs2 = ["aca","cba"]
	print Solution().longestCommonPrefix(strs)