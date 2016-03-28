import collections
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque()
        for i in xrange(len(nums)):
            q.append([[nums[i]], nums[:i]+nums[i+1:]])
        while q:
            n, tmp = q.popleft()
            if len(tmp) == 0:
                if n not in res:
                    res.append(n)
                continue
            for i in xrange(len(tmp)):                
                q.append([n+[tmp[i]], tmp[:i]+tmp[i+1:]])
        return res
