class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        res = []
        for k in xrange(n-1):
            l = k + 1
            r = n - 1
            while l < r:
                target = -k
                if nums[l] + nums[r] == target:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[k] > k:
                    r -= 1
                else:
                    l += 1
        return res