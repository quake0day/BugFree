class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p = 0
        for i in xrange(1, len(prices)):
            delta = prices[i] - prices[i-1]
            p += delta if delta > 0 else 0
        return p