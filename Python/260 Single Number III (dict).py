class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        table = {}
        for num in nums:
        	if num in table.keys():
        		del table[num]
        	else:
        		table[num] = 1
        return table.keys()


if __name__ == '__main__':
	nums = [1, 2, 1, 3, 2, 5]
	print Solution().singleNumber(nums)