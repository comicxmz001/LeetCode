class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dp = [0]
        for i in xrange(len(nums)):
            self.dp.append(self.dp[i] + nums[i])
        print self.dp

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
if __name__ == '__main__':
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print numArray.sumRange(0, 0)