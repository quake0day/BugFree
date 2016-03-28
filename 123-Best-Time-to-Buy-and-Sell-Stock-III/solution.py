class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        p1 = [0] * n
        p2 = [0] * n 
        l = prices[0]
        for i in xrange(1,n):
            l = min(l, prices[i])
            p1[i] = max(p1[i-1], prices[i]-l)
        r = prices[-1]
        for i in xrange(n-2, -1, -1):
            r = max(r, prices[i])
            p2[i] = max(p2[i+1], r - prices[i])
        res = 0
        for i in xrange(n):
            res = max(res, p1[i]+p2[i])
        return res