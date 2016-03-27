class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] < nums[r]:
                r = mid - 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                return nums[r]
        return nums[r]