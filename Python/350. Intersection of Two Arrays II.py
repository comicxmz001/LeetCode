class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        small = nums1 if len(nums1) < len(nums2) else nums2
        large = nums1 if len(nums1) >= len(nums2) else nums2

        res = []
        smallHash = {}
        for num in small:
        	if not num in smallHash:
        		smallHash[num] = 1
        	else:
        		smallHash[num] += 1

        for num in large:
        	if num in smallHash and smallHash[num]>0:
        		res.append(num)
        		smallHash[num] -= 1
        return res


if __name__ == '__main__':
	a = [1,2,2,1]
	b = [2]

	print Solution().intersect(a,b)