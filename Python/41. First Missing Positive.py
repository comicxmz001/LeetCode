#!/usr/bin/python

class Solution(object):
	    def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		for i in xrange(n):
			# this will put all the elements in their right places.
			# Attention: while (not if)
			while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
				t = nums[i] - 1
				nums[i],nums[t] = nums[t],nums[i]

		for i in xrange(n):
			if nums[i] != i + 1:
				return i + 1
		return n + 1
		
if __name__ == "__main__":
	nums = [3,4,-1,1]
	print Solution().firstMissingPositive(nums)