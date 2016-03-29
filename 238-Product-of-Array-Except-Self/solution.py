class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        
        for i in xrange(n-2, -1, -1):
            res[i] = nums[i+1] * res[i+1]
        left = 1
        for i in xrange(n):
            res[i] *= left
            left *= nums[i]
        return res