class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        if len(nums) == 1:
            res.append([nums[0]])
        else:
            for i in xrange(len(nums)):
                permuteList = self.permute(nums[:i]+nums[i+1:])
                # print permuteList
                for num in permuteList:
                    res.append([nums[i]]+num)
        return res

if __name__ == '__main__':
    print Solution().permute([1,2,3])