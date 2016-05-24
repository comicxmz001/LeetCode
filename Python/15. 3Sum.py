class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        l = len(nums)
        res = []
        for i in xrange(l-2):
            if i == 0 or (i>0 and nums[i]!= nums[i-1]):
                low = i + 1
                high = l - 1
                s = 0 - nums[i]
                while low < high:

                    if nums[low] + nums[high] == s:
                        res.append([nums[i],nums[low],nums[high]])
                        while low < high and nums[low+1] == nums[low]:
                            low += 1
                        while low < high and nums[high-1] == nums[high]:
                            high -= 1

                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < s:
                        low += 1
                    else:
                        high -= 1
        return res
                
            
arr = [-2,0,0,2,2]
print Solution().threeSum(arr)