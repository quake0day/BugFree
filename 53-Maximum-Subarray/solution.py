class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        l, r = 0, 0
        maxSum = nums[0]
        curSum = 0
        while r < n:
            curSum += nums[r]
            maxSum = max(curSum, maxSum)
            if curSum >= 0:
                r += 1
            else:
                curSum = 0
                r += 1
                l = r
        maxSum = max(maxSum, nums[r-1])
        return maxSum