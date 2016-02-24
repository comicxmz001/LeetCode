class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        version1 = version1.split('.')
        version2 = version2.split('.')

        for i in xrange(max(len(version1),len(version2))):
        	t1 = int(version1[i]) if i<len(version1) else 0
        	t2 = int(version2[i]) if i<len(version2) else 0

        	if t1>t2:
        		return 1
        	elif t1<t2:
        		return -1
        return 0

v1 = "1.123.523.5.23"
v2 = "1.2"
print Solution().compareVersion(v1,v2)