class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pos = self.partition(nums, 0, n-1)
        if pos > n - k:
            return self.findKthLargest(nums[:pos], k - (n - pos))
        elif pos < n - k:
            return self.findKthLargest(nums[pos+1:], k)
        else:
            return nums[pos]
    
    def partition(self, nums, l, r):
        pivot = nums[r]
        lo = l
        for i in xrange(l, r):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[r], nums[lo] = nums[lo], nums[r]
        return lo