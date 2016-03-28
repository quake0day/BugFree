class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, path, res):
            if len(path) == len(nums):
                res.append(path)
            
            i = 0
            while i < len(nums):
                if nums[i] not in path:
                    helper(nums, path+[i], res)
                while i + 1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1
                i += 1
        
        if not nums or len(nums) == 1:
            return [nums]
        nums = sorted(nums)
        res = []
        helper(nums, [], res)
        return res