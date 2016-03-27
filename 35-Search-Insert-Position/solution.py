class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] == target:
                return mid
            if l == r:
                return l + 1
            
            if nums[mid] > target:
                r = mid -1 
            elif nums[mid] < target:
                l = mid + 1
        
        return l + 1