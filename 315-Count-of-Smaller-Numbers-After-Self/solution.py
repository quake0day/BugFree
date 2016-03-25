class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        idxes = {}
        for k, v in enumerate(sorted(set(nums))):
            idxes[v] = k + 1
        iNums = [idxes[x] for x in nums]
        ft = BIT(len(iNums))
        ans = [0] * len(nums)
        for i in xrange(len(iNums) - 1, -1, -1):
            ans[i] = ft.sum(iNums[i] -1)
            ft.add(iNums[i], 1)
        return ans
        

class BIT(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)
        
    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += x & -x
    
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sums[x]
            x -= x & -x
        return res
