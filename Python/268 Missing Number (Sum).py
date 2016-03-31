class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0,1,...,n-1,n，sum of arrary (if no missing number) will be sum = n*(n+1)/2
        # delete all existing nums will leave the number that is missing from the array
        n = len(nums)
        sum = n*(n+1)/2
        for num in nums:
            sum -= num
        return sum
        
        # Note: This solution has an issue of over flow, if n is very large! 
        # XOR is a better choice