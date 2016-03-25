class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h = {}
        for i in xrange(len(nums)):
            if nums[i] in h and i - h[nums[i]] <= k:
                return True
            h[nums[i]] = i
        return False