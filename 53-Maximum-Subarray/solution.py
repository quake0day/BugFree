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
            if curSum >= 0:
                maxSum = max(curSum, maxSum)
                r += 1
            else:
                r += 1
                l = r
                
        return maxSum