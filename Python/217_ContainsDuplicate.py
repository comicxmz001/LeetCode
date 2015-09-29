class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		numdic = {}
		for item in nums:
			if item in numdic:
				return True
			numdic[item] = 1		
		return False

a1 = [1,4,5,4,5,4,5,4,5,4,5,4,5]
foo = Solution()
print foo.containsDuplicate(a1)