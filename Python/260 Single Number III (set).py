class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s1 = set(nums)
        s2 = set(nums)
        for num in nums:
            if num in s1:
                s1.remove(num)
            elif num in s2:
                s2.remove(num)
        res = s1 if s1 else s2
        return list(res)



if __name__ == '__main__':
	nums = [1, 2, 1, 3, 2, 5]
	print Solution().singleNumber(nums)