class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        threshold = int(len(nums)/2)
        hTable = {}
        for item in nums:
        	if item in hTable:
        		hTable[item] += 1
        		if hTable[item] > threshold:
        			return item
        		continue
        	hTable[item] = 1
        return

nums = [1,2,2,2,3]
foo = Solution()
print foo.majorityElement(nums)