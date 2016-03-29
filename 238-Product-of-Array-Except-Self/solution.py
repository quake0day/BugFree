import collections
import itertools 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        q = collections.deque(nums)
        n = len(nums)
        res = []
        tmp = []
        for i in xrange(1, n):
            q.rotate(1)
            tmp.append(list(q))
        tmp = list(zip(*tmp))
        for t in tmp:
            res.append(reduce(lambda x, y: x*y, t))
        return res