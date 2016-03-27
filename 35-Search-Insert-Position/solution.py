class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
            
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + r >> 1
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid 
            elif nums[mid] < target:
                l = mid 
        if nums[l] >= target:
            return l
        if nums[r] >= target:
            return r
        return len(nums)