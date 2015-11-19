class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
        	if nums2[n-1] >= nums1[m-1]:
        		nums1[m+n-1] = nums2[n-1]
        		n -= 1
        	else:
        		nums1[m+n-1] = nums1[m-1]
        		m -= 1
    	if n > 0:
    		nums1[:n] = nums2[:n]


if __name__ == '__main__':
	a1 = [1,2,3,0,0,0]
	a2 = [2,5,6]
	a3 = [1,0]
	a4 = [2]
	a5 = [4,0,0,0,0,0]
	a6 = [1,2,3,5,6]
	Solution().merge(a1,3,a2,3)
	print a1
	# Solution().merge(a3,1,a4,1)
	# print a3
	# Solution().merge(a5,1,a6,5)
	# print a5