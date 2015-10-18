class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_dic = {}
        for i in xrange(len(nums)):
        	if nums[i] in num_dic: #if already exists
        		if i - num_dic[nums[i]] <= k:
        			return True
        	num_dic[nums[i]] = i
        return False
    def main(self):
        a1 = [2,4,5,6,2,9]
        k = 4
        foo = Solution()
        print foo.containsNearbyDuplicate(a1, k)
if __name__ == "__main__":
    Solution().main()

