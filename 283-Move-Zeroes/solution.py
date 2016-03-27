class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        for r in xrange(1, len(nums)):
            if nums[r] != 0:
                while nums[l] != 0 and l < r:
                    l += 1
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
