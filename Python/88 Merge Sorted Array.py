class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and not n==0:
        	nums1[:n] = nums2[:n]
        	return None
        if n == 0:
        	return None
        j = 0
        k = 0
        for i in xrange(m+n):
        	if nums2[j] <= nums1[i]:
        		nums1[i:] = [nums2[j]] + nums1[i:-1]
        		j += 1
        	if i-j == m:
        		nums1[i:] = nums2[j:]
        		break
        	if j == n:
        		break


if __name__ == '__main__':
	a1 = [1,2,3,0,0,0]
	a2 = [2,5,6]
	a3 = [1,0]
	a4 = [2]
	a5 = [4,0,0,0,0,0]
	a6 = [1,2,3,5,6]
	Solution().merge(a1,3,a2,3)
	print a1
	Solution().merge(a3,1,a4,1)
	print a3
	Solution().merge(a5,1,a6,5)
	print a5