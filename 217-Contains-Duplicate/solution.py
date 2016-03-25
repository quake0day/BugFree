class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        h = {}
        for n in nums:
            if n in h:
                return True
            h[n] = True
        return False