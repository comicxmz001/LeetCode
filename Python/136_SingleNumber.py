class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Using XOR to find the single number.
        #Because every number appears twice, while N^N=0, 0^N=N,
        #XOR is cummutative, so the order of elements does not matter.
        #Finally, it will be res = 0 ^ singlenumber ==> res = singlenumber
        res = 0
        for num in nums:
            res ^= num
        return res

nums = [1,1,5,5,3,4,4,9,9,8,8,7,7]
foo = Solution()
print foo.singleNumber(nums)
