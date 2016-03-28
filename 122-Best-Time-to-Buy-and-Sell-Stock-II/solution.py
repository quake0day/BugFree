class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        q = collections.deque()
        q.append(prices)
        maxProfit = 0
        while q:
            prices = q.pop()
            if len(prices) == 0:
                continue
            profit, pair = self.helper(prices)
            maxProfit += profit
            q.append(prices[:pair[0]])
            q.append(prices[pair[1]:])
        return maxProfit
    
    
    def helper(self, prices):
        curMin = prices[0]
        maxProfit = 0
        pair = [0,0]
        for i in xrange(1, len(prices)):
            if prices[i] < curMin:
                curMin = prices[i]
                pair[0] = i
            if prices[i] - curMin > maxProfit:
                maxProfit = prices[i] - curMin
                pair[1] = i
        return maxProfit, pair
                