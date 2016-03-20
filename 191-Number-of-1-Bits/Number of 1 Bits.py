class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in xrange(32):
            count += (n >> i) & 1
        return count
        