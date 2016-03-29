class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = 0
        curMax = -float('inf')
        for i in xrange(len(nums)):
            curMax += nums[i]
            if curMax < 0:
                curMax = 0
            max_ = max(curMax, max_)
        return max_