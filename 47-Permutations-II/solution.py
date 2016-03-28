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
            if len(n) == len(nums):
                if n not in res:
                    res.append(n)
                    continue
            for i in xrange(len(tmp)):
                newn = n.append(tmp[i])
                ntmp = tmp[:i]+tmp[i+1:]
                q.append([newn, ntmp])
        return res