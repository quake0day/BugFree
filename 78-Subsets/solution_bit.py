class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        size = 2 ** n
        res = []
        for c in xrange(size):
            tmp = []
            for j in xrange(n):
                if c & (1 << j):
                    tmp.append(nums[j])
            res.append(sorted(tmp))
        return res