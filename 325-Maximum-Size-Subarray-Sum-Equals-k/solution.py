class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h ={0:-1}
        s = 0
        L = 0
        for i in xrange(len(nums)):
            s += nums[i]
            if s not in h:
                h[s] = i
            if (s - k) in h:
                idx = h[s-k]
                L = max(L, i - idx)
        return max(L, 0)
        
        