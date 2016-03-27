class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMin = nums[0]
        l, r = 0, len(nums) -1 
        while l <= r:
            mid = l + r >> 1
            if nums[mid] < curMin:
                curMin = nums[mid]
            if nums[mid] < nums[r]:
                r = mid - 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return curMin