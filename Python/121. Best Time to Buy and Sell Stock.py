class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minBuy = 999999 # probably should use sys.maxint
        maxProfits = 0
        
        for i in xrange(len(prices)):
            minBuy = min(minBuy, prices[i])
            maxProfits = max(maxProfits, prices[i] - minBuy)
        return maxProfits
            
        